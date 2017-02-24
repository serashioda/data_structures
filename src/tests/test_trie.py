"""Test for Trie implementation."""

import pytest
import random
from trie import Trie


@pytest.fixture
def full_trie():
    """Fixture to return full trie."""
    from trie import Trie
    trie = Trie()
    all_words = []
    with open('/usr/share/dict/words') as a:
        for line in a:
            if "'" not in line:
                all_words.append(line.strip('\n'))
    words = []
    for x in range(0, 200):
        word = random.choice(all_words)
        trie.insert(word)
        words.append(word)
    return trie, words


@pytest.fixture
def empty_trie():
    """Fixture to return empty trie."""
    trie = Trie()
    return trie


def test_full_trie_traverse(full_trie):
    t = full_trie[0]
    word = full_trie[1][0]
    result = t.traverse(word[0])
    t = list(result)


def test_empty_trie():
    t = Trie()
    res = t.traverse('meow')
    assert res == None


def test_one_letter_trie():
    t = Trie()
    t.insert('m')
    res = t.traverse('m')
    assert res == None


def test_insert_1_words(empty_trie):
    """Test insert method."""
    empty_trie.insert('amos')
    assert empty_trie.root == {'a': {'m': {'o': {'s': {'$': None}}}}}


def test_insert_5_words(empty_trie):
    """Test insert method."""
    empty_trie.insert('amos')
    empty_trie.insert('soma')
    empty_trie.insert('bob')
    empty_trie.insert('dole')
    empty_trie.insert('oi')
    trie = {'a': {'m': {'o': {'s': {'$': None}}}},
            'b': {'o': {'b': {'$': None}}},
            'd': {'o': {'l': {'e': {'$': None}}}},
            'o': {'i': {'$': None}},
            's': {'o': {'m': {'a': {'$': None}}}}}
    assert empty_trie.root == trie


def test_size(full_trie):
    """Test size method returns 200 on 200 size trie."""
    assert full_trie[0].size() == 200


def test_remove(full_trie):
    """Test removing string from tried."""
    word = random.choice(full_trie[1])
    full_trie[0].remove(word)
    assert not full_trie[0].contains(word)


def test_remove_error(empty_trie):
    """Test removing string
     from tried."""
    empty_trie.insert('amos')
    empty_trie.insert('soma')
    with pytest.raises(KeyError):
        empty_trie.remove('apples')


def test(empty_trie):
    """."""
    empty_trie.insert('teapot')
    empty_trie.insert('teabag')
    empty_trie.insert('teabat')
    words = empty_trie.autocomplete('tea')
    for word in words:
        assert word in ['teabat', 'teabag', 'teapot']
        print(word)
