"""Tests for Hash Table ."""

import pytest
import random


@pytest.fixture
def full_hash_table():
    """Fixture to return full hash_table."""
    from hash_table import HashTable
    ht = HashTable(300)
    all_words = []
    with open('/usr/share/dict/words') as a:
        for line in a:
            if "'" not in line:
                all_words.append(line.strip('\n'))
    words = []
    for x in range(0, 2000):
        word = random.choice(all_words)
        ht.set(word, word + ' key')
        words.append(word)
    return ht, words


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


def test_get(full_hash_table):
    """Test get 300000 times."""
    for x in range(1, 300000):
        word = random.choice(full_hash_table[1])
        k_v = full_hash_table[0].get(word)
        assert word == k_v[0] and word + ' key' == k_v[1]


def test_not_found_raise_error(full_hash_table):
    """Test not found raise error."""
    with pytest.raises(KeyError):
        full_hash_table[0].get('Aweasdkjasdsome')
