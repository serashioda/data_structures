"""Tests for Hash Table ."""


def test_hash_table_hash_method():
    """Test hash method."""
    from hash_table import HashTable
    hash_table = HashTable(10)
    hash_num = hash_table._hash('hello_world')
    assert hash_num == 1179


def test_hash_table_hash_method_diff():
    """Test hash method on diffrent key."""
    from hash_table import HashTable
    hash_table = HashTable(10)
    hash_num = hash_table._hash('hello_bob')
    assert hash_num == 934
