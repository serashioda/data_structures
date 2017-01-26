"""Trie implementation."""


class Trie(object):
    """Trie Class."""

    def __init__(self):
        """Initialize a root for Trei."""
        self.root = {}
        self._size = 0

    def insert(self, string):
        """Insert string into trie."""
        current = self.root
        for char in string.lower():
            current = current.setdefault(char, {})
        current.setdefault("$")
        self._size += 1

    def contains(self, string):
        """Return True if string in the trie."""
        current = self.root
        for char in string.lower():
            # if char not in current:
            #     return False
            current = current[char]
        if "$" in current:
            return True
        return False

    def size(self):
        """Return size of trie."""
        return self._size

    def _return_dict(self, string):
        current = self.root
        for char in string.lower():
            current = current[char]
        if "$" in current:
            return True
        return current

    def traverse(self, dict):
        """Return path."""

    def depth_first_traversal(self, string):
        """."""
        return self.traverse(self._return_dict(string))
