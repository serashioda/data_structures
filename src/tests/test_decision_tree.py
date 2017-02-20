"""Test for decision tree."""

from sklearn import tree, datasets

iris = datasets.load_iris()

clf = tree.DecisionTreeClassifier()

data1 = iris['data'][:49]
target1 = iris['target'][:49]

test_data1 = iris['data'][49:50]
test_target1 = iris['target'][49:50]

data2 = iris['data'][50:99]
target2 = iris['target'][50:99]

test_data2 = iris['data'][99:100]
test_target2 = iris['target'][99:100]


clf = clf.fit(data1 + data2, target1 + target2)

import ipdb; ipdb.set_trace()
