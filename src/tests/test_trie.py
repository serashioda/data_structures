"""Test for Trie implementation."""

import pytest
import random


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
    from trie import Trie
    trie = Trie()
    return trie


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


def test_contains_random(full_trie):
    """Test contains method on random 200 words."""
    assert full_trie[0].contains(random.choice(full_trie[1]))


def test_size(full_trie):
    """Test size method returns 200 on 200 size trie."""
    assert full_trie[0].size() == 200
