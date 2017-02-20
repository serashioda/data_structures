"""Implemention of K Nearest Neighbour Classifier."""

import numpy as np


class Knn(object):
    """K Nearest Neigbour Classifier."""

    def __init__(self, dataset, k=5):
        """Initialize classifier with dateset and k integer."""
        if type(k) is not int or k > len(dataset) or k < 0:
            raise ValueError("k must be an integer between 1 and the length of the dataset")
        self.dataset = dataset
        self.k = 5

    def _distance(self, p, q):
        """Calculate the distance between two points."""
        return np.sqrt(np.sum((p - q)**2))

    def predict(self, data):
        """Given a data point, predict the class of that data, based on dataset."""
        for num in data:
            lst = []
            for row in self.dataset:
                lst.append((self._distance(num, row[:-1]), row[-1]))
            neighbors = sorted(lst)[:self.k]
            classes = [x[1] for x in neighbors]
            return max(set(classes), key=classes.count)
