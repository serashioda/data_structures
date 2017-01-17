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
