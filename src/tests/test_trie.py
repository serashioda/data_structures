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
    for x in range(1, 200):
        word = random.choice(all_words)
        trie.insert(word)
        words.append(word)
    return trie, words
