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
            if char in current:
                current = current[char]
            else:
                return False
        return "$" in current

    def size(self):
        """Return size of trie."""
        return self._size

    def remove(self, string):
        """Remove given string from trie. Raise excepion if non-existant."""
        current = self.root
        for idx, char in enumerate(string.lower()):
            if (idx + 1) == len(string) and '$' in current[string[-1]]:
                del current[string[-1]]['$']
                return
            current = current[char]
        raise KeyError("Cannot remove string not in trie")
