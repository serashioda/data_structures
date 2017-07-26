"""Module with implementation of KMeans."""


def load_csv(filename, cols=()):
    """Load and covert from csv."""
    import numpy as np
    data = np.loadtxt(filename,
                      delimiter=',',
                      usecols=cols)
    return data


class KMeansClassifier(object):
    """
    Unsupervised clustering algorithm.

    clf = KMeansClassifier(max_iter=None, min_step='auto')
        -max_iter: the number of iterations before the algorithm stops
        -min_step: the smallest distance between an old centroid
                   and a new centroid before the algorithm stops.
                   - If 'auto', min_step is calculated to be 1/1000th of largest first step.

    clf.fit(data, k=2)
        -k: number of nodes to generate

    clf.predict(data)
    """
