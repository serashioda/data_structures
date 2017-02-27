"""Trie implementation. Speed is O(n)."""


class Trie(object):
    """Trie Class."""

    def __init__(self):
        """Initialize a root for Trei."""
        self.root = {}
        self._size = 0

    def insert(self, string=''):
        """Insert string into trie."""
        current = self.root
        for char in string.lower():
            current = current.setdefault(char, {})
        current.setdefault("$")
        self._size += 1

    def contains(self, string=''):
        """Return True if string in the trie."""
        current = self.root
        for char in string.lower():
            if char not in current:
                return False
            current = current[char]
        if "$" in current:
            return True
        return False

    def size(self):
        """Return size of trie."""
        return self._size

    def remove(self, string=''):
        """Remove given string from the trie. Raise excepion if word doesn't exist."""
        current = self.root
        fragment = ''
        for idx, char in enumerate(string.lower()):
            fragment += char
            words = list(self.autocomplete(fragment))
            if len(words) == 1:
                # We've reached the fork of this word, delete the entire fork
                self._size -= 1
                del current[char]
                return
            if (idx + 1) == len(string) and '$' in current[string[-1]]:
                self._size -= 1
                del current[string[-1]]['$']
                return
            if char not in current:
                raise KeyError("Cannot remove string not in trie")
            current = current[char]
