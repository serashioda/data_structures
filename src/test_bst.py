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
