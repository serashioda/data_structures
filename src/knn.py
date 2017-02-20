"""Implemention of K Nearest Neighbour Classifier."""

import numpy as np


class Knn(object):
    """K Nearest Neigbour Classifier."""

    def __init__(self, dataset, k=5):
        """Initialize classifier with dateset and k integer."""
        if k > len(dataset) or k < 0 or type(k) is not int:
            raise ValueError("k must be an integer between 1 and the length of the dataset")
        self.dataset = dataset
        self.k = 5

    def _distance(self, p, q):
        """Calculate the distance between two points."""
        return np.sqrt(np.sum((p - q)**2))
