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
            current = current[char]
        if "$" in current:
            return None
        return False

    def size(self):
        """Return size of trie."""
        return self._size

    def remove(self, string=''):
        """Remove given string from the trie. Raise excepion if word doesn't exist."""
        current = self.root
        for idx, char in enumerate(string.lower()):
            if (idx + 1) == len(string) and '$' in current[string[-1]]:
                del current[string[-1]]['$']
                return
            current = current[char]
        raise KeyError("Cannot remove string not in trie")

    def _return_dict(self, string=''):
        current = self.root
        for char in string.lower():
            current = current[char]
        if "$" in current:
            return None
        return current

    def traverse(self, start):
        """Traverse and return individual letters."""
        from pprint import pprint
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
        from pprint import pprint
        current = self.root
        for char in string.lower():
            current = current[char]
        if "$" in current:
            return None
        path = []
        not_visited = [{a: current[a]} for a in current]

        result = []
        self.get_words(string, not_visited, result)

        pprint(result)

        return (y for y in result)

    def get_words(self, word, trie, result):
        """."""
        for group in trie:
            # import pdb; pdb.set_trace()

            for letter in group:
                if letter is "$":
                    result.append(word)
                else:
                    # import pdb; pdb.set_trace()
                    self.get_words(word + letter, [group[letter]], result)
