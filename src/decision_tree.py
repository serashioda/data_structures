"""Implementation of a decision tree."""


class TreeNode(object):
    """Tree Node for decision trees."""

    def __init__(self, column=None, split=None, left=None, right=None, data_idx=None):
        """Initialize variables for tree node."""
        self.column = column
        self.split = split
        self.left = left
        self.right = right
        self.data_idx = data_idx


class DecisionTree(object):
    """Decision Tree Class."""

    def __init__(self, max_depth=None, min_leaf_size=1):
        """."""
        self.max_depth = max_depth
        self.min_leaf_size = min_leaf_size
        self.root = None

    def fit(self, input_df, labels):
        """Method for fittting a new tree."""
        self.root = TreeNode(data_idx=input_df)
        # start spliting
        self._split(self.root)

    def predict(self, columns):
        """Given some data seperated into columns.

        return new labels for data given.
        """
        pass

    def _split(self, node):
        """Given some node containing data.

        find best column to split on and assign split point and child nodes.
        """
        column, split_point = self._best_split_point_algorithm()
#         put column and split_point
#         if result of spliting produces nodes with atleast one values:
#             node.left = TreeNode()
#             node.right = TreeNode()
#         if left has one value or right is purely one label:
#             end left
#         if right has one value or right is purely one label:
#             end right
        pass

    def gini(self, p):
        """Given a dataset return same data set giniafide."""
        return (p) * (1 - (p)) + (1 - p) * (1 - (1 - p))

    def _best_split_point_algorithm():
        pass
