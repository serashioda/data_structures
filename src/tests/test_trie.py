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


def test_remove_non_existant_word():
    """Check that removing a non-existing word raises a KeyError."""
    t = Trie()
    with pytest.raises(KeyError):
        t.remove('meow')


def test_traverse_random_word(full_trie):
    """Check that given a random word from the system dictionary, it can correct find it."""
    t = full_trie[0]
    word = full_trie[1][0]
    result = t.traverse(word[0])
    matched_word = False
    for letter in result:
        pos = letter
        for c in word[1:]:
            if c not in pos:
                # skip word, 2nd character isn't the one we're looking for
                break
            matched_word = True
            pos = pos[c]
            assert pos is not None

    assert matched_word is True


def test_traverse_empty_trie():
    """Test the traverse returns None on an empty trie."""
    t = Trie()
    res = t.traverse('meow')
    assert res is None


def test_contains_empty():
    """Test that contains returns false on an empty trie."""
    t = Trie()
    assert t.contains("dasda") is False


def test_contains_simple():
    """Test the border condition of one word in the trie."""
    t = Trie()
    t.insert("meowmix")
    assert t.contains("meowmix") is True


def test_autocomplete_empty():
    """Test autocomplete returns None if there are no items in the Trie."""
    t = Trie()
    assert t.autocomplete("dasdas") is None


def test_traverse_simple():
    """Test traverse returns a correct tree given a simple input."""
    t = Trie()
    t.insert('meow')
    t.insert('mexico')
    t.insert('mera')
    t.insert('repo')
    res = t.traverse('m')

    for letter in res:
        assert letter['e'] is not None
        assert letter['e']['r'] is not None
        assert letter['e']['r']['a'] is not None
        assert letter['e']['r']['a']['$'] is None

        assert letter['e']['x'] is not None
        assert letter['e']['x']['i'] is not None
        assert letter['e']['x']['i']['c'] is not None
        assert letter['e']['x']['i']['c']['o'] is not None
        assert letter['e']['x']['i']['c']['o']['$'] is None

        assert letter['e']['o'] is not None
        assert letter['e']['o']['w'] is not None
        assert letter['e']['o']['w']['$']is None


def test_size_simple(full_trie):
    """Test size reports the correct value inserting and removing values."""
    words = full_trie[1]
    t = Trie()
    count = 0
    assert t.size() == count

    for word in words:
        t.insert(word)
        count += 1
        assert t.size() == count

    for word in words:
        t.remove(word)
        count -= 1
        assert t.size() == count


def test_traverse_simple_non_existant_root():
    """."""
    t = Trie()
    t.insert('abc')
    t.insert('bed')
    t.insert('fek')
    res = t.traverse('m')
    assert res is None


def test_traverse_with_non_matching_root():
    """Test traverse does not return other words from the trie."""
    t = Trie()
    t.insert('abc')
    t.insert('bed')
    t.insert('fek')
    res = t.traverse('a')

    for letter in res:
        assert letter['b'] is not None
        assert letter['b']['c'] is not None
        assert letter['b']['c']['$'] is None

        # check other words didn't make it in
        assert 'f' not in letter
        assert 'e' not in letter
        assert 'k' not in letter


def test_traverse_with_none_root():
    """Test traverse with None returns None."""
    t = Trie()
    assert t.traverse(None) is None


def test_traverse_with_emptystring_root():
    """Test that traverse with emptystring returns None."""
    t = Trie()
    assert t.traverse('') is None


def test_one_letter_trie():
    """."""
    t = Trie()
    t.insert('m')
    res = t.traverse('m')
    assert res is None


def test_insert_1_words(empty_trie):
    """Test insert of a simple word sets root to the correct value."""
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
    """Test removing string from tried."""
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
