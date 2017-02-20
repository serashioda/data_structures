"""Test K-nearest neighbors classifier."""

import pytest
import numpy as np


@pytest.fixture
def knn():
    """Create a Knn to run tests on."""
    from knn import Knn
    from sklearn import datasets
    iris = datasets.load_iris()
    data1 = iris['data'][:49]
    target1 = iris['target'][:49]

    data2 = iris['data'][50:99]
    target2 = iris['target'][50:99]

    targets = np.append(target1, target2).reshape(98, 1)
    data = np.append(data1, data2, 0)

    data = np.append(
        data,
        targets,
        1
    )
    return (
        Knn(data),
        (iris['data'][49:50], iris['target'][49:50][0]),
        (iris['data'][99:100], iris['target'][99:100][0])
    )


def test_predict_setosa(knn):
    """Test predict setosa."""
    classifier = knn[0]
    prediction = classifier.predict(knn[2][0])
    assert prediction == knn[2][1]


def test_predict_versicolor(knn):
    """Test predict versicolor."""
    classifier = knn[0]
    prediction = classifier.predict(knn[1][0])
    assert prediction == knn[1][1]


def test_bad_k_letter():
    """Test k as letter raises error."""
    from knn import Knn
    with pytest.raises(ValueError):
        Knn([1, 2, 3, 4], k='q')


def test_bad_k_bigger_than_dataset():
    """Test bad k bigger than dataset."""
    from knn import Knn
    with pytest.raises(ValueError):
        Knn([1, 2, 3, 4], k=6)


def test_bad_k_lower_than_one():
    """Test bad k lower than one."""
    from knn import Knn
    with pytest.raises(ValueError):
        Knn([1, 2, 3, 4], k=-2)
