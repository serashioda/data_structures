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
            if len(words) == 1 and words[0] == string:
                # We've reached the fork of this word, delete the entire fork
                self._size -= 1
                del current[char]
                return
            if char not in current:
                raise KeyError("Cannot remove string not in trie")
            current = current[char]

    def traverse(self, start):
        """Traverse and return individual letters."""
        if start is None or start is '':
            return None
        current = self.root
        for char in start.lower():
            if char not in current:
                return None
            current = current[char]
        if "$" in current:
            return None
        children = [{a: current[a]} for a in current]
        return (y for y in children)

    def autocomplete(self, string=''):
        """Traverse and return whole words."""
        if len(self.root) == 0:
            return None
        current = self.root
        for char in string.lower():
            current = current[char]
        not_visited = [{a: current[a]} for a in current]

        result = []
        self.get_words(string, not_visited, result)

        return (y for y in result)

    def get_words(self, word, trie, result):
        """Traverse and return all words for the given tree."""
        for group in trie:
            for letter in group:
                if letter is "$":
                    result.append(word)
                else:
                    self.get_words(word + letter, [group[letter]], result)
