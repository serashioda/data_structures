"""Implementation of a decision tree."""


class TreeNode(object):
    """Tree Node for decision trees."""

    def __init__(self, data, split_value, split_gini, split_col, left=None, right=None, parent=None):
        """Initialize a node object for a decision tree classifier."""
        self.left = left
        self.right = right
        self.data = data
        self.split_value = split_value
        self.split_gini = split_gini
        self.split_col = split_col


class DecisionTree(object):
    """Decision Tree Class."""

    def __init__(self, max_depth=None, min_leaf_size=1):
        """."""
        self.max_depth = max_depth
        self.min_leaf_size = min_leaf_size
        self.root = None

    def fit(self, data):
        """Create a tree to fit the data."""
        split_col, split_value, split_gini, split_groups = self._get_split(data)
        new_node = TreeNode(data, split_value, split_gini, split_col)
        if not self.root:
            self.root = new_node

    def _test_split(self, index, value, dataset):
        """Split a dataset based on an attribute and an attribute value."""
        left, right = list(), list()
        for row in dataset:
            if row[index] < value:
                left.append(row)
            else:
                right.append(row)
        return left, right

    def _gini_index(self, groups, class_values):
        """Calculate the Gini index for a split dataset."""
        gini = 0.0
        for class_value in class_values:
            for group in groups:
                size = len(group)
                if size == 0:
                    continue
                proportion = [row[-1] for row in group].count(class_value) / float(size)
                gini += (proportion * (1.0 - proportion))
        return gini

    def _get_split(self, dataset):
        """Select the best split point for a dataset."""
        class_values = list(set(row[-1] for row in dataset))
        b_index, b_value, b_score, b_groups = 999, 999, 999, None
        for index in range(len(dataset[0]) - 1):
            for row in dataset:
                groups = self._test_split(index, row[index], dataset)
                gini = self._gini_index(groups, class_values)
                print('X%d < %.3f Gini=%.3f' % ((index + 1), row[index], gini))
                if gini < b_score:
                    b_index, b_value, b_score, b_groups = index, row[index], gini, groups
        return b_index, b_value, b_score, b_groups
