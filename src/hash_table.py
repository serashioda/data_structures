"""Hash Table implementation."""


class HashTable(object):
    """Class HashTable."""

    def __init__(self, num):
        """Initialize with number of slots to be in table."""
        self.table = []
        for x in range(0, num):
            self.table.append([])

    def _hash(self, key):
        """Hash the key provided and return."""
        hash_val = 0
        for char in key:
            hash_val += ord(char)
        return hash_val

    def _xor_hash(self, key):
        """XOR hash the key provided and return."""
        hash_val = 0
        for char in key:
            hash_val ^= ord(char)
        return hash_val

    def set(self, key, val):
        """Store the given val using the given key."""
        hash_num = self._hash(key) % len(self.table)
        self.table[hash_num].append((key, val))

    def get(self, key):
        """Return the value stored with the given key."""
        pass
