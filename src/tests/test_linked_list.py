"""Tests for our linked_list module."""

import pytest
from linked_list import LinkedList
from linked_list import Node


def test_linked_list():
    """Test the instantiation of our Linked List."""
    from linked_list import LinkedList
    lst = LinkedList()
    if lst._head is None:
        pass


def test_insertion_constructor():
    """Test insertion constructor works properly."""
    l = LinkedList([1, 2, 3])
    assert l._head.val == 3


def test_insertion_constructor_none():
    """Test insertion constructor works properly."""
    l = LinkedList(None)
    assert l._head is None


def test_base_push():
    """Test a non-init'd linked list handles edge condition."""
    l = LinkedList()
    assert l.size() == 0
    l.push(100)
    assert l.size() == 1
    assert l.pop() == 100


def test_range_large_insert():
    """Test that linked list works with over 10000 inserts and removals."""
    l = LinkedList()
    for i in range(1, 10000):
        l.push(i)
        assert l.size() == i
        node = l.search(i)
        assert node is not None

    for i in range(9999, 0, -1):
        node = l.search(i)
        assert node.val == i
        l.remove(node)
        assert l.size() == i - 1

    assert l.size() == 0


def test_display_range():
    """Test that display correct displays node in order of insertion."""
    l = LinkedList()
    assert l.display() == '()'
    l.push(1)
    assert l.display() == '(1)'
    l.push(2)
    assert l.display() == '(2, 1)'
    l.push(3)
    assert l.display() == '(3, 2, 1)'
    l.push('pug')
    assert l.display() == '(\'pug\', 3, 2, 1)'
    l.push('dog')
    assert l.display() == '(\'dog\', \'pug\', 3, 2, 1)'


def test_remove():
    """Test that remove correctly removes an element from the list."""
    l = LinkedList()
    for i in range(0, 100):
        l.push(i)
    node = l.search(42)
    assert node is not None
    l.remove(node)
    assert l.search(42) is None


def test_node():
    """Test the instantiation of a node."""
    new_node = Node(1, 2)
    assert new_node.val == 1 and new_node.next == 2


def test_push_linked_list():
    """Test the push method in our LinkedList class."""
    lst = LinkedList()
    lst.push(2)
    assert lst._head.val == 2


def test_remove_invalid_input():
    l = LinkedList()
    with pytest.raises(ValueError):
        l.remove(42)


def test_pop_linked_list():
    """Test pop method in our LinkedList class."""
    from linked_list import LinkedList
    lst = LinkedList()
    with pytest.raises(IndexError):
        lst.pop()


def test_size():
    """Test size method on LinkedList class."""
    from linked_list import LinkedList
    lst = LinkedList()
    lst.push(2)
    lst.push(3)
    lst.push(4)
    assert lst.size() == 3


def test_size_empty():
    """Test size method for empty linked list."""
    from linked_list import LinkedList
    lst = LinkedList()
    assert lst.size() == 0


def test_size_one():
    """Test size method for list with one node."""
    from linked_list import LinkedList
    lst = LinkedList()
    lst.push(4)
    assert lst.size() == 1


def test_search_linked_list_empty():
    """Test search method in our LinkedList class."""
    from linked_list import LinkedList
    lst = LinkedList()
    assert lst.search(2) is None


def test_search_linked_list_single():
    """Test search method in our LinkedList class."""
    from linked_list import LinkedList
    lst = LinkedList()
    lst.push(3)
    assert lst.search(3) is not None


def test_search_linked_list_multi():
    """Test search method in our LinkedList class."""
    from linked_list import LinkedList
    lst = LinkedList()
    lst.push(1)
    lst.push(2)
    lst.push(3)
    assert lst.search(2) is not None


def test_remove_linked_list_single():
    """Test remove method in our LinkedList class."""
    from linked_list import LinkedList
    lst = LinkedList()
    lst.push(2)
    node = lst.search(2)
    assert node is not None
    lst.remove(node)
    assert lst.size() == 0


def test_remove_linked_list_multi():
    """Test remove method in our LinkedList class."""
    from linked_list import LinkedList
    lst = LinkedList()
    lst.push(5)
    lst.push(2)
    node = lst.search(2)
    assert node is not None
    lst.remove(node)
    assert lst.size() == 1


def tests_display_empty():
    """Test display method for empty linked list."""
    from linked_list import LinkedList
    lst = LinkedList()
    assert lst.display() == "()"


def tests_display_one():
    """Test display method for list with one node."""
    from linked_list import LinkedList
    lst = LinkedList()
    lst.push(2)
    assert lst.display() == "(2)"
