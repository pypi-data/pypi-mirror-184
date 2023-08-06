"""Module containing the decision tree classifier and regressor implementations."""

import logging
from copy import deepcopy
from operator import ge, lt
from statistics import mean, mode

import numpy as np
import pandas as pd
from pandas.api.types import is_numeric_dtype
from sklearn.metrics import accuracy_score, mean_squared_error

from .base_estimator import DecisionTreeEstimator, Node

logging.basicConfig(
    level=logging.DEBUG, format="%(message)s", filename="debug.log", filemode="w"
)


class DecisionTreeClassifier(DecisionTreeEstimator):
    """A Decision Tree Classifier"""

    def __init__(self, *, criterion=None):
        super().__init__(metric=self._find_entropy, criterion=criterion)

    def _find_entropy(self, X, y):
        """Measures the amount of impurity in (X, y)."""
        proba = np.unique(y, return_counts=True)[1] / len(X)
        return -np.sum(proba * np.log2(proba))

    def _find_rem(self, X, y, d):
        """Measures the entropy after testing feature (d)."""
        weight = np.unique(X[d], return_counts=True)[1] / len(X)
        metric = [
            self._metric(X.loc[X[d] == t], y.loc[X[d] == t]) for t in np.unique(X[d])
        ]
        return np.sum(weight * metric)

    def _find_information_gain(self, X, y, d):
        """Measures the reduction in the overall entropy by testing on feature."""
        if is_numeric_dtype(X[d]):
            gain, optimal_threshold, rem = super()._find_optimal_threshold(X, y, d)
            self._n_thresholds[d] = optimal_threshold
            logging.info("%s = %d - %d = %d", d, self._metric(X, y), rem, gain)
            return gain

        gain = self._metric(X, y) - self._find_rem(X, y, d)
        logging.info(
            "%s = %d - %d = %d", d, self._metric(X, y), self._find_rem(X, y, d), gain
        )
        return gain

    def fit(self, X, y):
        """Fits the decision tree classifier to the dataset."""
        if X.empty or y.empty:
            raise Exception("Dataset is empty")

        self._n_levels = {
            d: ((lt, ge) if is_numeric_dtype(X[d]) else np.unique(X[d]))
            for d in X.columns
        }

        self._root = self._make_tree(X, y)
        return self

    def _make_tree(self, X, y, *, parent=None, branch=None, depth=0):
        """Performs the ID3 algorithm.

        Base Cases
        ----------
        - All instances have the same labels.
        - Dataset is empty.
        - If all feature values are identical.
        - Max depth reached.
        - Max number of instances in partitioned dataset reached.
        """

        def make_node(value):
            return Node(
                data=(X, y),
                value=value,
                branch=branch,
                parent=parent,
                depth=depth,
            )

        if len(np.unique(y)) == 1:
            logging.info("All instances have the same labels (%s)", y.iat[0])
            return make_node(y.iat[0])
        if X.empty:
            logging.info("Dataset is empty")
            return make_node(mode(parent.y))
        if all((X[d] == X[d].iloc[0]).all() for d in X.columns):
            logging.info("All instances have the same descriptive features")
            return make_node(mode(y))
        if self._criterion.get("max_depth", float("inf")) <= depth:
            logging.info("Stopping at Max Depth")
            return make_node(mode(y))
        if self._criterion.get("min_samples_split", float("-inf")) >= len(X):
            logging.info("Stopping at %d instances", len(X))
            return make_node(mode(y))

        logging.info("===Information Gain===\n")
        max_gain = np.argmax([self._find_information_gain(X, y, d) for d in X.columns])

        if self._criterion.get("min_gain", float("-inf")) >= max_gain:
            logging.info("Stopping at Information Gain=%d", max_gain)
            return make_node(mode(y))

        best_feature = X.columns[max_gain]
        logging.info("\nBest Feature = %s", best_feature)

        best_node = deepcopy(make_node(best_feature))

        if is_numeric_dtype(X[best_feature]):
            best_node.threshold = round(self._n_thresholds[best_feature], 2)

        levels = [
            self._partition_data(X, y, best_feature, level, best_node.threshold)
            for level in self._n_levels[best_feature]
        ]

        for *d, level in levels:
            logging.info("\n===Partitioned Dataset (%s)===\n", level)
            logging.info("%s\n", str(pd.concat(d, axis=1).head()))

            best_node += self._make_tree(
                *d, parent=best_node, branch=level, depth=depth + 1
            )
        return best_node

    def score(self, X, y):
        """Evaluates the decision tree model on the test set."""
        y_hat = self.predict(X)
        return accuracy_score(y, y_hat)


class DecisionTreeRegressor(DecisionTreeEstimator):
    """A Decision Tree Regressor"""

    def __init__(self, *, criterion=None):
        super().__init__(metric=self._find_variance, criterion=criterion)

    def _find_variance(self, X, y):
        """Computes the variance from a random sample on each target level."""
        if len(X) == 1:
            logging.info("Variance = 0")
            return 0
        logging.info(
            "Variance = %f / %d", np.sum([(t - mean(y)) ** 2 for t in y]), len(X) - 1
        )
        return np.sum([(t - mean(y)) ** 2 for t in y]) / (len(X) - 1)

    def _find_weighted_variance(self, X, y, d):
        """Computes the weighted variance from a random sample on each target level."""
        if is_numeric_dtype(X[d]):
            gain, optimal_threshold, _ = super()._find_optimal_threshold(X, y, d)
            self._n_thresholds[d] = optimal_threshold
            return gain

        def weight(t):
            return len(X.loc[X[d] == t]) / len(X)

        return np.sum(
            [
                weight(t) * self._find_variance(X.loc[X[d] == t], y.loc[X[d] == t])
                for t in np.unique(X[d])
            ]
        )

    def fit(self, X, y):
        """Fits the decision tree regressor to the dataset."""
        if X.empty or y.empty:
            raise Exception("Dataset is empty")

        self._n_levels = {
            d: ((lt, ge) if is_numeric_dtype(X[d]) else np.unique(X[d]))
            for d in X.columns
        }

        self._root = self._make_tree(X, y)
        return self

    def _make_tree(self, X, y, *, branch=None, parent=None, depth=0):
        """Performs the ID3 algorithm.

        Base Cases
        ----------
        - All instances have the labels.
        - Dataset is empty.
        - Max depth reached.
        - Min number of instances in partitioned dataset reached.
        """

        def make_node(value):
            return Node(
                data=(X, y),
                value=value,
                branch=branch,
                parent=parent,
                depth=depth,
            )

        if y.empty:
            return make_node(mean(parent.y))
        if len(np.unique(y)) == 1:
            logging.info("All instances have the same labels (%s)", str(y.iat[0]))
            return make_node(y.iat[0])
        if X.empty:
            logging.info("Dataset is empty")
            return make_node(mean(y))
        if self._criterion.get("max_depth", float("inf")) <= depth:
            logging.info("Stopping at Max Depth")
            return make_node(mean(y))
        if self._criterion.get("min_samples_split", float("-inf")) >= len(X):
            logging.info("Stopping at %d instances", len(X))
            return make_node(mean(y))

        logging.info("===Information Gain===\n")

        min_var = np.argmin([self._find_weighted_variance(X, y, d) for d in X.columns])
        logging.info("Min Var = %f", min_var)

        best_feature = X.columns[min_var]
        logging.info("Best Feature = %s", best_feature)

        best_node = deepcopy(make_node(best_feature))

        if is_numeric_dtype(X[best_feature]):
            best_node.threshold = round(self._n_thresholds[best_feature], 2)

        levels = [
            self._partition_data(X, y, best_feature, level, best_node.threshold)
            for level in self._n_levels[best_feature]
        ]

        for *d, level in levels:
            logging.info("\n===Partitioned Dataset (%s)===\n", level)
            logging.info("%s\n", str(pd.concat(d, axis=1).head()))

            best_node += self._make_tree(
                *d, parent=best_node, branch=level, depth=depth + 1
            )
        return best_node

    def score(self, X, y):
        """Evaluates the decision tree model on the test set."""
        y_hat = self.predict(X)
        return mean_squared_error(y, y_hat, squared=False)
