"""Module containing the parallel decision tree classifier implementation."""


from copy import deepcopy
from operator import ge, lt
from statistics import mode

import numpy as np
from mpi4py import MPI
from pandas.api.types import is_numeric_dtype
from sklearn.metrics import accuracy_score

from .base_estimator import DecisionTreeEstimator, Node

world_comm = MPI.COMM_WORLD
world_rank = world_comm.Get_rank()
world_size = world_comm.Get_size()


class ParallelDecisionTreeClassifier(DecisionTreeEstimator):
    """A Parallel Decision Tree Classifier"""

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
            gain, optimal_threshold, _ = super()._find_optimal_threshold(X, y, d)
            self._n_thresholds[d] = optimal_threshold
            return gain

        gain = self._metric(X, y) - self._find_rem(X, y, d)
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

    def _make_tree(self, X, y, *, comm=world_comm, parent=None, branch=None, depth=0):
        """Performs the ID3 algorithm.

        Base Cases
        ----------
        - All instances have the same labels.
        - Dataset is empty.
        - If all feature values are identical.
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

        rank = comm.Get_rank()
        size = comm.Get_size()

        if len(np.unique(y)) == 1:
            return make_node(y.iat[0])
        if X.empty:
            return make_node(mode(parent.y))
        if all((X[d] == X[d].iloc[0]).all() for d in X.columns):
            return make_node(mode(y))
        if self._criterion.get("max_depth", float("inf")) <= depth:
            return make_node(mode(y))
        if self._criterion.get("min_samples_split", float("-inf")) >= len(X):
            return make_node(mode(y))

        max_gain = np.argmax([self._find_information_gain(X, y, d) for d in X.columns])

        if self._criterion.get("min_gain", float("-inf")) >= max_gain:
            return make_node(mode(y))

        best_feature = X.columns[max_gain]
        best_node = deepcopy(make_node(best_feature))

        if is_numeric_dtype(X[best_feature]):
            best_node.threshold = round(self._n_thresholds[best_feature], 2)

        levels = [
            self._partition_data(X, y, best_feature, level, best_node.threshold)
            for level in self._n_levels[best_feature]
        ]

        if size == 1:
            for *d, level in levels:
                best_node += self._make_tree(
                    *d, comm=comm, parent=best_node, branch=level, depth=depth + 1
                )
        else:
            psize = size // len(levels)
            color = rank // psize % len(levels)
            key = rank % psize + psize * (rank >= psize * len(levels))

            group = comm.Split(color, key)
            *d, level = levels[color]

            sub_tree = comm.allgather(
                {
                    level: self._make_tree(
                        *d, comm=group, parent=best_node, branch=level, depth=depth + 1
                    )
                }
            )

            best_node.children |= {k: v for d in sub_tree for k, v in d.items()}
            group.Free()
        return best_node

    def score(self, X, y):
        """Evaluates the decision tree model on the test set."""
        y_hat = self.predict(X)
        return accuracy_score(y, y_hat)
