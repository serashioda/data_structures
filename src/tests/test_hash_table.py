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


def test_hash_table_xor_hash_method():
    """Test xor hash method."""
    from hash_table import HashTable
    hash_table = HashTable(10)
    hash_num = hash_table._xor_hash('hello_world')
    assert hash_num == 95


def test_hash_table_xor_hash_method_diff():
    """Test xor hash method."""
    from hash_table import HashTable
    hash_table = HashTable(10)
    hash_num = hash_table._xor_hash('hello_bob')
    assert hash_num == 82


def test_hash_table_set_method():
    """Test set method."""
    from hash_table import HashTable
    hash_table = HashTable(10)
    hash_num = hash_table._hash('hello_world')
    num = hash_num % len(hash_table.table)
    hash_table.set('hello_world', 4)
    assert hash_table.table[num] == [('hello_world', 4)]


def test_has_table_get_method():
    """Test get method."""
    from hash_table import HashTable
    hash_table = HashTable(10)
    hash_table.set('hello_potato', 5)
    assert hash_table.get('hello_potato') == ('hello_potato', 5)
