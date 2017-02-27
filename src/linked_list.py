"""Module defining linked list."""


class LinkedList(object):
    """Classic linked list data structure."""

    def __init__(self, iterable=None):
        """Initialize LinkedList instance."""
        self._head = None
        self._length = 0
        if iterable is not None:
            for el in iterable:
                self.push(el)

    def push(self, val):
        """Insert val at the head of linked list."""
        self._head = Node(val, self._head)
        self._length += 1

    def pop(self):
        """Pop the first value off of the head and return it."""
        if self._head is None:
            raise IndexError("Cannot pop from an empty linked list.")
        first = self._head.val
        self._head = self._head.next
        self._length -= 1
        return first

    def size(self):
        """Return length of linked list."""
        return self._length

    def search(self, val):
        """Will return the node from the list if present, otherwise none."""
        search = self._head
        while search:
            if search.val == val:
                return search
            search = search.next
        return None

    def remove(self, node):
        """Remove a node from linked list."""
        if type(node) is Node:
            prev = None
            curr = self._head
            while curr:
                if curr is node:
                    if prev:
                        prev.next = curr.next
                    else:
                        self._head = curr.next
                    self._length -= 1
                    break
                prev = curr
                curr = curr.next
        else:
            raise ValueError("Argument to remove must be of node type.")

    def display(self):
        """Display linked list in tuple literal form."""
        res = "("
        curr = self._head
        while curr:
            val = curr.val
            if type(val) is str:
                val = "'" + val + "'"
            else:
                val = str(val)
            res += val
            if curr.next:
                res += ', '
            curr = curr.next
        return res + ')'


class Node(object):
    """Node class."""

    def __init__(self, val, next=None):
        """Initialize Node instance."""
        self.val = val
        self.next = next
