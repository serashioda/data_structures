"""Tests for Hash Table ."""


class HashTable(object):
    """Class HashTable."""

    def __init__(self, num):
        """Initialize with number of slots to be in table."""
        self.table = []
        for x in range(0, num):
            self.table.append([])

    def _hash(self, key):
        """Sash the key provided and return."""
        pass

    def set(self, key, val):
        """Store the given val using the given key."""
        pass

    def get(self, key):
        """Return the value stored with the given key."""
        pass
