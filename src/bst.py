"""Implementation of a Binary Search Tree."""

from my_queue import Queue
from stack import Stack


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
        self._size = 0

    def insert(self, val):
        """Insert value into Binary Search Tree."""
        if not self.contains(val):
            if not self.root:
                self.root = Node(val)
            else:
                self._insert_node(val, self.root)
            self._size += 1

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

    def contains(self, val):
        """Return True if val is in the BST, False if not."""
        return self.search(val) is not None

    def balance(self):
        """Return 1, 0 or -1 that represents how well balanced the tree is."""
        if self.root is None:
            return 0
        return self._depth_node(self.root.leftChild) - self._depth_node(self.root.rightChild)

    def size(self):
        """Return size of bst."""
        return self._size

    def search(self, val):
        """Search if node exist in tree and return if present, otherwise None."""
        curr_node = self.root
        while curr_node:
            if curr_node.val == val:
                return curr_node
            elif val > curr_node.val:
                curr_node = curr_node.rightChild
            else:
                curr_node = curr_node.leftChild
        return None

    def breadthfirst(self):
        """Breadth First Traversal for Binary Search Tree."""
        q = Queue()
        q.enqueue(self.root)
        while q.size():
            node = q.dequeue()
            yield node.val
            if node.leftChild is not None:
                q.enqueue(node.leftChild)
            if node.rightChild is not None:
                q.enqueue(node.rightChild)

    def preorder(self):
        """Preorder generator."""
        node = self.root
        if node is None:
            return
        s = Stack()
        s.push(node)
        while s.size():
            node = s.pop()
            yield node.val
            if node.rightChild is not None:
                s.push(node.rightChild)
            if node.leftChild is not None:
                s.push(node.leftChild)

    def postorder(self):
        """Postorder generator."""
        node = self.root
        s = []
        last_visited = None
        while s or node is not None:
            if node is not None:
                s.append(node)
                node = node.leftChild
            else:
                peek_node = s[-1]
                if peek_node.rightChild is not None and last_visited is not peek_node.rightChild:
                    node = peek_node.rightChild
                else:
                    yield peek_node.val
                    last_visited = s.pop()

    def inorder(self):
        """In order generator."""
        node = self.root
        s = Stack()
        while s.size() or node is not None:
            if node is not None:
                s.push(node)
                node = node.leftChild
            else:
                node = s.pop()
                yield node.val
                node = node.rightChild

    def delete(self, val):
        """Delete a node."""
        if self.root is None:
            return None
        elif self.root.val == val:
            self._size -= 1
            if self.root.leftChild is None and self.root.rightChild is None:
                self.root = None
            elif self.root.leftChild and self.root.rightChild is None:
                self.root = self.root.leftChild
            elif self.root.rightChild and self.root.rightChild is None:
                self.root = self.root.rightChild
            else:
                del_node_parent = self.root
                del_node = self.root.rightChild
                while del_node.leftChild:
                    del_node_parent = del_node
                    del_node = del_node.leftChild

                self.root.val = del_node.val
                if del_node.rightChild:
                    if del_node_parent.val > del_node.val:
                        del_node_parent.leftChild = del_node.rightChild
                    elif del_node_parent.val < del_node.val:
                        del_node_parent.rightChild = del_node.rightChild
                    else:
                        del_node_parent.rightChild = None
                        del_node_parent = del_node.rightChild
                else:
                    if del_node.val < del_node_parent.val:
                        del_node_parent.leftChild = None
                    else:
                        del_node_parent.rightChild = None

            return

        parent = None
        node = self.root

        while node and node.val != val:
            parent = node
            if val < node.val:
                node = node.leftChild
            elif val > node.val:
                node = node.rightChild

        # if node not found in tree
        if node is None:
            return None

        # if node to delete has no children
        elif node.leftChild is None and node.rightChild is None:
            if val < parent.val:
                parent.leftChild = None
            else:
                parent.rightChild = None

        # node to delete has only a left child
        elif node.leftChild and node.rightChild is None:
            if val < parent.val:
                parent.leftChild = node.leftChild
            else:
                parent.rightChild = node.leftChild

        # node to delete has only a right child
        elif node.rightChild and node.leftChild is None:
            if val < parent.val:
                parent.leftChild = node.rightChild
            else:
                parent.rightChild = node.rightChild

        # node to delete has both left and right children
        else:
            del_node_parent = node
            del_node = node.rightChild
            while del_node.leftChild:
                del_node_parent = del_node
                del_node = del_node.leftChild

            node.val = del_node.val
            if del_node.rightChild:
                if del_node_parent.val > del_node.val:
                    del_node_parent.leftChild = del_node.rightChild
                elif del_node_parent.val < del_node.val:
                    del_node_parent.rightChild = del_node.rightChild
            else:
                if del_node.val < del_node_parent.val:
                    del_node_parent.leftChild = None
                else:
                    del_node_parent.rightChild = None
        self._size -= 1

    def right_rotation(self, node):
        """Right rotation."""
        if self.root == node:
            self.root = node.rightChild
            node.rightChild = None
            self.root.leftChild = node
        else:
            parent = self.root
            while parent:
                if parent.rightChild == node:
                    break
                elif parent.leftChild == node:
                    break
                elif node.val > parent.val:
                    parent = parent.rightChild
                else:
                    parent = parent.leftChild
            temp_node = node.rightChild
            parent.rightChild = temp_node
            temp_node.leftChild = node
            node.rightChild = None

    def left_rotation(self, node):
        """Left rotation."""
        if self.root == node:
            self.root = node.leftChild
            node.leftChild = None
            self.root.rightChild = node
        else:
            parent = self.root
            while parent:
                if parent.rightChild == node:
                    break
                elif parent.leftChild == node:
                    break
                elif node.val > parent.val:
                    parent = parent.rightChild
                else:
                    parent = parent.leftChild
            temp_node = node.leftChild
            parent.leftChild = temp_node
            temp_node.rightChild = node
            node.leftChild = None
