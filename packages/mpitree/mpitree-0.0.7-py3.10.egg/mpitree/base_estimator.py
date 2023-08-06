"""Module containing the `Node` and `BaseEstimator` implementations."""

from __future__ import annotations

import sys
from dataclasses import dataclass, field
from itertools import starmap
from operator import eq, ge, lt
from typing import Optional, Union

import numpy as np
import pandas as pd
from pandas.api.types import is_numeric_dtype


@dataclass(kw_only=True)
class Node:
    """A Decision Tree Node.

    Parameters
    ----------
    value : str, float, default=None
        - the descriptive or target feature value of a node.

    threshold : float, default=None
        - the feature value to partition the dataset into two levels with some range.

    branch : str, default=None
        - the feature value on a split from the parent node on a feature value.

    parent : Node, default=None
        - the precedent node along the path from the root to a node.

    depth : int, default=0
        - the number of levels from the root to a node.

    children : dict, default={}
        - the nodes on each split of the parent node for each unique feature values.
    """

    value: Union[str, float] = None
    threshold: Optional[float] = None
    branch: str = field(default_factory=str)
    parent: Optional[Node] = None
    depth: int = field(default_factory=int)
    children: dict = field(default_factory=dict)

    def __str__(self):
        """Displays the nodes properties."""
        spacing = self.depth * "|  " + ("└── " if self.is_leaf else "├── ")

        if not self.parent:
            return spacing + f"{self.value}"
        if self.threshold is not None:
            if self is self.parent.left:
                return spacing + f"{self.value} [{list(self.children.keys())[0]}]"
            if self is self.parent.right:
                return spacing + f"{self.value} [{list(self.children.keys())[1]}]"
        return spacing + f"{self.value} [{self.branch}]"

    def __eq__(self, other: Node):
        """Checks if two nodes are the same.

        >>> Node() == Node()
        True
        >>> Node(value="Alice") != Node(value="Bob")
        True
        >>> Node() == "Not a Node"
        Traceback (most recent call last):
            ...
        TypeError: Object is not a `Node` instance
        """
        if not isinstance(self, type(other)):
            raise TypeError("Object is not a `Node` instance")
        return self.__dict__ == other.__dict__

    def __add__(self, other: Node):
        """Adds another node to a node's children.

        >>> (Node() + Node(branch="< 0")).is_leaf
        False
        >>> Node() + Node()
        Traceback (most recent call last):
            ...
        AttributeError: Object's `branch` attribute is not instantiated
        >>> Node() + "Not a Node"
        Traceback (most recent call last):
            ...
        TypeError: Object is not a `Node` instance
        """
        if not isinstance(self, type(other)):
            raise TypeError("Object is not a `Node` instance")
        if not other.branch:
            raise AttributeError("Object's `branch` attribute is not instantiated")

        other.parent = self
        self.children[other.branch] = other
        return self

    @property
    def is_leaf(self):
        """Returns whether a node is terminal.

        >>> Node().is_leaf
        True
        >>> not Node(children={"A": Node()}).is_leaf
        True
        """
        return not self.children

    @property
    def left(self):
        """Returns the left child of a numeric-featured node.

        >>> Node().left is None
        True
        >>> Node(threshold=0, children={"< 0": 0}).left
        0
        """
        return self.children.get(f"< {self.threshold}")

    @property
    def right(self):
        """Returns the right child of a numeric-feature node.

        >>> Node().right is None
        True
        >>> Node(threshold=0, children={">= 0": 0}).right
        0
        """
        return self.children.get(f">= {self.threshold}")


class DecisionTreeEstimator:
    """A Decision Tree Estimator"""

    def __init__(self, *, metric=None, criterion=None):
        """
        Parameters
        ----------
        root : Node
            - the starting node with depth zero of a decision tree.

        n_levels : dict
            - contains a list of all unique feature values for each descriptive feature.

        n_thresholds : dict
            - contains the possible splits of the continuous feature being tested.

        metric : {_find_entropy, _find_variance}
            - a measure of impurity.

        criterion {'max_depth', 'min_samples_split', 'min_gain'}
            - contains options for pre-pruning
        """

        self._root = None
        self._n_levels = None
        self._n_thresholds = {}
        self._metric = metric
        self._criterion = criterion

    def __iter__(self, node=None):
        if not node:
            node = self._root

        yield node
        for child in node.children.values():
            yield from self.__iter__(child)

    def __str__(self):
        """Pre-order traversal a decision tree."""
        if not self._check_is_fitted:
            raise AttributeError("Decision tree is not fitted")
        return "\n".join(map(str, self))

    def __eq__(self, other: DecisionTreeEstimator):
        """Checks if two decision trees are identical."""
        if not isinstance(self, type(other)):
            raise TypeError("Object is not a 'DecisionTreeEstimator' instance")
        if not self._check_is_fitted or not other._check_is_fitted:
            raise AttributeError("At least one 'DecisionTreeEstimator' is not fitted")

        return all(starmap(eq, zip(self, other)))

    @property
    def _check_is_fitted(self):
        """Checks whether a decision tree is fitted."""
        return type(self._root) is Node

    def fit(self, X, y):
        if X.empty or y.empty:
            raise Exception("Expected at least one sample in both `X` and `y`")

        if self._criterion is None:
            self._criterion = {}
        elif not type(self._criterion) is dict:
            raise TypeError("Expected `criterion` parameter to be `dict` type")

        self._n_levels = {
            d: ((lt, ge) if is_numeric_dtype(X[d]) else np.unique(X[d]))
            for d in X.columns
        }

    def _find_optimal_threshold(self, X, y, d):
        """Computes the optimal threshold between different target levels instances."""
        df = pd.concat([X, y], axis=1)
        df.sort_values(by=[d], inplace=True)

        thresholds = []
        for i in range(len(df) - 1):
            pairs = df.iloc[i : i + 2, -1]
            if any(pairs.iloc[0] != val for val in pairs.values):
                thresholds.append(df.loc[pairs.index, d].mean())

        levels = []
        for threshold in thresholds:
            level = df.loc[df[d] < threshold], df.loc[df[d] >= threshold]
            weight = np.array([len(i) / len(df) for i in level])

            metric_total = self._metric(df.iloc[:, :-1], df.iloc[:, -1])
            metric_partial = [
                self._metric(level[0].iloc[:, :-1], level[0].iloc[:, -1]),
                self._metric(level[1].iloc[:, :-1], level[1].iloc[:, -1]),
            ]

            rem = weight.dot(metric_partial)
            levels.append(metric_total - rem)

        return max(levels), thresholds[np.argmax(levels)], rem

    def _partition_data(self, X, y, d, op, threshold=None):
        """Returns a subset of the training data with feature (d) and level (t)."""
        if threshold:
            return (
                *list(map(lambda f: f.loc[op(X[d], threshold)], [X, y])),
                f"{'<' if op is lt else '>='} {threshold}",
            )
        idx = X[d] == op
        return X.loc[idx].drop(d, axis=1), y.loc[idx], op

    def predict(self, x):
        """Predicts a test sample on a decision tree."""
        node = self._root
        while not node.is_leaf:
            query_branch = x[node.value].values[0]

            if is_numeric_dtype(query_branch):
                next_node = node.left if query_branch < node.threshold else node.right
            else:
                try:
                    next_node = node.children[query_branch]
                except KeyError:
                    sys.exit(f"Branch {node.value} -> {query_branch} does not exist")
            node = next_node
        return node.value


if __name__ == "__main__":
    import doctest

    doctest.testmod()
