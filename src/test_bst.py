"""Tests for Binary Search Tree."""

import pytest


@pytest.fixture
def empty_bst():
    """Create a Binary Search Tree and return it."""
    from bst import BinarySearchTree
    return BinarySearchTree()


def test_insert_one(empty_bst):
    """Test inserting one value."""
    empty_bst.insert(8)
    assert empty_bst.root.val == 8


def test_insert_two(empty_bst):
    """Test inserting two values."""
    empty_bst.insert(8)
    empty_bst.insert(10)
    assert empty_bst.root.rightChild.val == 10


def test_insert_three(empty_bst):
    """Test inserting three values."""
    empty_bst.insert(8)
    empty_bst.insert(10)
    empty_bst.insert(3)
    assert empty_bst.root.leftChild.val == 3


def test_insert_six_right(empty_bst):
    """Test inserting 6 values last three inserted to the right of the root node."""
    empty_bst.insert(8)
    empty_bst.insert(10)
    empty_bst.insert(3)
    empty_bst.insert(17)
    empty_bst.insert(9)
    empty_bst.insert(32)
    assert empty_bst.root.rightChild.rightChild.val == 17
    assert empty_bst.root.rightChild.rightChild.rightChild.val == 32
    assert empty_bst.root.rightChild.leftChild.val == 9


def test_insert_six_left(empty_bst):
    """Test inserting 6 values last three inserted to the left of the root node."""
    empty_bst.insert(8)
    empty_bst.insert(10)
    empty_bst.insert(3)
    empty_bst.insert(6)
    empty_bst.insert(4)
    empty_bst.insert(2)
    assert empty_bst.root.leftChild.leftChild.val == 2
    assert empty_bst.root.leftChild.rightChild.leftChild.val == 4
    assert empty_bst.root.leftChild.rightChild.val == 6


def test_size(empty_bst):
    """Test size with 9 nodes."""
    empty_bst.insert(8)
    empty_bst.insert(10)
    empty_bst.insert(3)
    empty_bst.insert(1)
    empty_bst.insert(6)
    empty_bst.insert(14)
    empty_bst.insert(4)
    empty_bst.insert(7)
    empty_bst.insert(13)
    assert empty_bst.size() == 9


def test_depth_3(empty_bst):
    """Test depth method on 3 depth tree."""
    empty_bst.insert(8)
    empty_bst.insert(10)
    empty_bst.insert(3)
    empty_bst.insert(1)
    empty_bst.insert(6)
    empty_bst.insert(14)
    empty_bst.insert(4)
    empty_bst.insert(7)
    empty_bst.insert(13)
    assert empty_bst.depth() == 3


def test_contains_is_false(empty_bst):
    """Test when val is not in BST."""
    empty_bst.insert(8)
    assert empty_bst.contains(8)


def test_contains_is_true(empty_bst):
    """Test when val is in BST."""
    assert empty_bst.size() == 0


def test_search_curr_node(empty_bst):
    """Test if node exiss in tree."""
    empty_bst.insert(5)
    empty_bst.insert(7)
    empty_bst.insert(4)
    assert empty_bst.contains(4)
    assert empty_bst.contains(5)
    assert empty_bst.contains(7)


def test_search_curr_node_is_none(empty_bst):
    """Test if node exiss in tree."""
    assert empty_bst.contains(9) is False


def test_balance_curr_node_is_none(empty_bst):
    """Test if node exiss in tree."""
    assert empty_bst.balance() == 0


def test_balance_equal_curr_node(empty_bst):
    """Test if node exiss in tree."""
    empty_bst.insert(5)
    empty_bst.insert(7)
    empty_bst.insert(4)
    assert empty_bst.balance() == 0


def test_balance_two_node(empty_bst):
    """Test finding blance from a two node tree."""
    empty_bst.insert(10)
    empty_bst.insert(15)
    assert empty_bst.balance() == -1


def test_balance_two_nodes_negative(empty_bst):
    """Test finding blance from a two node tree."""
    empty_bst.insert(10)
    empty_bst.insert(2)
    assert empty_bst.balance() == 1


def test_find_balance_balanced_three_node(empty_bst):
    """Test finding balance from a balanced three node tree."""
    empty_bst.insert(10)
    empty_bst.insert(15)
    empty_bst.insert(5)
    assert empty_bst.balance() == 0


def test_not_balanced(empty_bst):
    """Test finding balance from a not balanced three node tree."""
    empty_bst.insert(5)
    empty_bst.insert(15)
    empty_bst.insert(10)
    assert empty_bst.balance() == -2


def test_breath_first(empty_bst):
    """Test breath first on 9 size tree."""
    empty_bst.insert(8)
    empty_bst.insert(10)
    empty_bst.insert(3)
    empty_bst.insert(1)
    empty_bst.insert(6)
    empty_bst.insert(14)
    empty_bst.insert(4)
    empty_bst.insert(7)
    empty_bst.insert(13)
    breadth_first_comprension = [num for num in empty_bst.breadth_first()]
    assert breadth_first_comprension == [8, 3, 10, 1, 6, 14, 4, 7, 13]
