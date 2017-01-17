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

    def depth(self):
        """Call helper depth method."""
        return self._depth_node(self.root) - 1

    def _depth_node(self, root, depth=0):
        """Depth method the takes in root node."""
        if root is None:
            return depth
        return max(self._depth_node(root.leftChild, depth + 1),
                   self._depth_node(root.rightChild, depth + 1))

    def balance(self):
        """Return 1, 0 or -1 that represents how well balanced the tree is."""
        if self.root is None:
            return 0
        return self._depth_node(self.root.rightChild) - self._depth_node(self.root.leftChild)

    def size(self):
        """Return size of bst."""
        return self.size

    def search(self, val):
        """Search if node exist in tree and reuturn if present, otherwise None."""
        curr_node = self.root
        while curr_node:
            if curr_node.val == val:
                return curr_node
            elif curr_node.val > val:
                curr_node == curr_node.rightChild
            else:
                curr_node == curr_node.leftChild
            curr_node = curr_node.next
        return None
