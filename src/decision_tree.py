"""Implementation of a decision tree."""

from sklearn import tree, datasets

from sklearn.externals.six import StringIO
import pydotplus

iris = datasets.load_iris()

clf = tree.DecisionTreeClassifier()

data1 = iris['data'][:48]

test_data1 = iris['data'][48:50]

data2 = iris['data'][50:98]

test_data2 = iris['data'][98:100]

del iris['data'][48:50]

clf = clf.fit(, iris['target'][:100])

import pdb; pdb.set_trace()

dot_data = StringIO()

tree.export_graphviz(
    clf,
    out_file=dot_data,
    feature_names=iris.feature_names,
    class_names=iris.target_names[:2],
    filled=True,
    rounded=True,
    impurity=False
)
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
graph.write_pdf('iris.pdf')
