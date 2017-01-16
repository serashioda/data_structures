"""Implementation of a Binary Search Tree."""


class Node(object):
    """Node class."""

    def __init__(self, val):
        """Node instantiation."""
        self.val = val
        self.leftChild = None
        self.rightChild = None


class BinarySearchTree(object):
    """Binary Search Tree Class."""

    def __init__(self):
        """Binary Search Tree instantiation."""
        self.root = None
        self.size = 0

    def insert(self, val):
        """Insert value into Binary Search Tree."""
        if not self.root:
            self.root = Node(val)
        else:
            self._insert_node(val, self.root)
        self.size += 1

    def _insert_node(self, val, node):
        """Insert a node when not at the root."""
        if val < node.val:
            if node.leftChild:
                self._insert_node(val, node.leftChild)
            else:
                node.leftChild = Node(val)
        else:
            if node.rightChild:
                self._insert_node(val, node.rightChild)
            else:
                node.rightChild = Node(val)
