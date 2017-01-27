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
            current = current[char]
        if "$" in current:
            return True
        return False

    def size(self):
        """Return size of trie."""
        return self._size

    def remove(self, string):
        """Remove given string from the trie. Raise excepion if word doesn't exist."""
        current = self.root
        for idx, char in enumerate(string.lower()):
            if (idx + 1) == len(string) and '$' in current[string[-1]]:
                del current[string[-1]]['$']
                return
            current = current[char]
        raise KeyError("Cannot remove string not in trie")

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
        from pprint import pprint
        current = self.root
        for char in string.lower():
            current = current[char]
        if "$" in current:
            return True
        path = []
        not_visited = [{a: current[a]} for a in current]
        # import pdb; pdb.set_trace()
        while not_visited:
            pprint(not_visited)
            print('\n')
            cur = not_visited.pop()
            for sub_tree in cur:
                if sub_tree is not '$':
                    path.append(sub_tree)
                    not_visited.append(cur[sub_tree])
        print(path)
