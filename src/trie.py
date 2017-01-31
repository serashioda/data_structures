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
        error = KeyError('{} not in trie.'.format(string))
        current = self.root
        path = [current]
        for char in string.lower():
            if char in current:
                current = current[char]
            else:
                raise error
            path.append(current)
        else:
            if "$" not in current:
                raise error
            deleted_dicts = []
            for current_dict, char in zip(reversed(path[:-1]), reversed(string)):
                if len(current_dict[char]) <= 1:
                    deleted_dicts.append((current_dict, char))
                else:
                    break
            if len(deleted_dicts) > 0:
                del deleted_dicts[-1][0][deleted_dicts[-1][1]]
