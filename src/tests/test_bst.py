"""Tests for Binary Search Tree."""

import pytest


@pytest.fixture
def empty_bst():
    """Create a Binary Search Tree and return it."""
    from bst import BinarySearchTree
    return BinarySearchTree()


@pytest.fixture
def bst_1():
    """Create a Binary Search Tree and return it."""
    from bst import BinarySearchTree
    b_s_t = BinarySearchTree()
    b_s_t.insert(8)
    b_s_t.insert(10)
    b_s_t.insert(3)
    b_s_t.insert(1)
    b_s_t.insert(6)
    b_s_t.insert(14)
    b_s_t.insert(4)
    b_s_t.insert(7)
    b_s_t.insert(13)
    return b_s_t


@pytest.fixture
def bst_2():
    """Create a Binary Search Tree and return it."""
    from bst import BinarySearchTree
    b_s_t = BinarySearchTree()
    b_s_t.insert(36)
    b_s_t.insert(3)
    b_s_t.insert(14)
    b_s_t.insert(26)
    b_s_t.insert(5)
    b_s_t.insert(4)
    b_s_t.insert(11)
    b_s_t.insert(40)
    b_s_t.insert(52)
    b_s_t.insert(94)
    b_s_t.insert(74)
    return b_s_t


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


def test_size(bst_1):
    """Test size with 9 nodes."""
    assert bst_1.size() == 9


def test_depth_3(bst_1):
    """Test depth method on 3 depth tree."""
    assert bst_1.depth() == 3


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


def test_breath_first(bst_1):
    """Test breath_first traversal on bst_1."""
    breadth_first_comprehension = [num for num in bst_1.breadthfirst()]
    assert breadth_first_comprehension == [8, 3, 10, 1, 6, 14, 4, 7, 13]


def test_breath_first_different(bst_2):
    """Test breath_first traversal on bst_2."""
    breadth_first_comprehension = [num for num in bst_2.breadthfirst()]
    assert breadth_first_comprehension == [36, 3, 40, 14, 52, 5, 26, 94, 4, 11, 74]


def test_pre_order(bst_1):
    """Test pre_order traversal on bst_1."""
    pre_order_comprension = [num for num in bst_1.preorder()]
    assert pre_order_comprension == [8, 3, 1, 6, 4, 7, 10, 14, 13]


def test_pre_order_diffrent(bst_2):
    """Test pre_order traversal on bst_2."""
    pre_order_comprension = [num for num in bst_2.preorder()]
    assert pre_order_comprension == [36, 3, 14, 5, 4, 11, 26, 40, 52, 94, 74]


def test_in_order(bst_1):
    """Test in_order traversal on bst_1."""
    in_order_comprension = [num for num in bst_1.inorder()]
    assert in_order_comprension == [1, 3, 4, 6, 7, 8, 10, 13, 14]


def test_in_order_diffrent(bst_2):
    """Test in_order traversal on bst_2."""
    in_order_comprension = [num for num in bst_2.inorder()]
    assert in_order_comprension == [3, 4, 5, 11, 14, 26, 36, 40, 52, 74, 94]


def test_post_order(bst_1):
    """Test post_order traversal on bst_1."""
    in_order_comprension = [num for num in bst_1.postorder()]
    assert in_order_comprension == [1, 4, 7, 6, 3, 13, 14, 10, 8]


def test_post_order_diffrent(bst_2):
    """Test post_order traversal on bst_1."""
    in_order_comprension = [num for num in bst_2.postorder()]
    assert in_order_comprension == [4, 11, 5, 26, 14, 3, 74, 94, 52, 40, 36]


def test_delete_one_node(empty_bst):
    """Test delete on one node in bst."""
    empty_bst.insert(1)
    empty_bst.delete(1)
    assert empty_bst.root is None


def test_delete_two_children_right_child(empty_bst):
    """Test delete on one node with two children and successor has right child."""
    empty_bst.insert(10)
    empty_bst.insert(5)
    empty_bst.insert(15)
    empty_bst.insert(18)
    empty_bst.insert(12)
    empty_bst.insert(13)
    empty_bst.delete(15)
    in_order_comprension = [num for num in empty_bst.inorder()]
    assert in_order_comprension == [5, 10, 12, 13, 18]


def test_delete_two_children_not_right_child(empty_bst):
    """Test delete on one node with two children."""
    empty_bst.insert(10)
    empty_bst.insert(5)
    empty_bst.insert(15)
    empty_bst.insert(18)
    empty_bst.insert(12)
    empty_bst.delete(15)
    in_order_comprension = [num for num in empty_bst.inorder()]
    assert in_order_comprension == [5, 10, 12, 18]


def test_delete_root_bst_1(bst_1):
    """Test delete root on bst_1."""
    in_order_comprension = [num for num in bst_1.inorder()]
    assert 8 in in_order_comprension
    bst_1.delete(8)
    assert 8 not in [num for num in bst_1.inorder()]


def test_delete_root_bst_2(bst_2):
    """Test delete root on bst_2."""
    in_order_comprension = [num for num in bst_2.inorder()]
    assert 36 in in_order_comprension
    bst_2.delete(36)
    assert 36 not in [num for num in bst_2.inorder()]


def test_delete_bst_1(bst_1):
    """Test delete on bst_1."""
    bst_1.delete(8)
    bst_1.delete(10)
    bst_1.delete(3)
    bst_1.delete(6)
    bst_1.delete(1)
    bst_1.delete(14)
    bst_1.delete(4)
    bst_1.delete(7)
    bst_1.delete(13)
    in_order_comprension = [num for num in bst_1.inorder()]
    assert in_order_comprension == []


def test_delete_bst_2(bst_2):
    """Test delete on bst_2."""
    bst_2.delete(36)
    bst_2.delete(3)
    bst_2.delete(14)
    bst_2.delete(26)
    bst_2.delete(5)
    bst_2.delete(4)
    bst_2.delete(11)
    bst_2.delete(40)
    bst_2.delete(52)
    bst_2.delete(94)
    bst_2.delete(74)
    in_order_comprension = [num for num in bst_2.inorder()]
    assert in_order_comprension == []


def test_delete_one_child_right_subtree(empty_bst):
    """Test delete has one child in roots right subtree."""
    empty_bst.insert(10)
    empty_bst.insert(11)
    empty_bst.insert(9)
    empty_bst.insert(7)
    empty_bst.insert(13)
    empty_bst.delete(11)
    in_order_comprension = [num for num in empty_bst.inorder()]
    assert in_order_comprension == [7, 9, 10, 13]


def test_delete_one_child_left_subtree(empty_bst):
    """Test delete has one child in roots left subtree."""
    empty_bst.insert(10)
    empty_bst.insert(11)
    empty_bst.insert(9)
    empty_bst.insert(7)
    empty_bst.insert(13)
    empty_bst.delete(9)
    in_order_comprension = [num for num in empty_bst.inorder()]
    assert in_order_comprension == [7, 10, 11, 13]


def test_delete_leaf_node_right_subtree(empty_bst):
    """Test delete leaf node."""
    empty_bst.insert(10)
    empty_bst.insert(11)
    empty_bst.insert(9)
    empty_bst.insert(7)
    empty_bst.insert(13)
    empty_bst.delete(13)
    in_order_comprension = [num for num in empty_bst.inorder()]
    assert in_order_comprension == [7, 9, 10, 11]


def test_delete_leaf_node_left_subtree(empty_bst):
    """Test delete leaf node."""
    empty_bst.insert(10)
    empty_bst.insert(11)
    empty_bst.insert(9)
    empty_bst.insert(7)
    empty_bst.insert(13)
    empty_bst.delete(7)
    in_order_comprension = [num for num in empty_bst.inorder()]
    assert in_order_comprension == [9, 10, 11, 13]


# def test_left_rotation_root(empty_bst):
#     """Test left rotation on simple tree."""
#     empty_bst.insert(1)
#     empty_bst.insert(2)
#     empty_bst.insert(3)
#     empty_bst.left_rotation(empty_bst.root)
#     # import pdb; pdb.set_trace()
#     breadthfirst_comprension = [num for num in empty_bst.breadthfirst()]
#     assert breadthfirst_comprension == [2, 1, 3]


def test_left_rotation_not_root(empty_bst):
    """Test left rotation on simple tree."""
    empty_bst.insert(1)
    empty_bst.insert(2)
    empty_bst.insert(3)
    empty_bst.left_rotation(empty_bst.root)
    breadthfirst_comprension = [num for num in empty_bst.breadthfirst()]
    assert breadthfirst_comprension == [2, 1, 3]
    empty_bst.insert(4)
    empty_bst.insert(5)
    empty_bst.left_rotation(empty_bst.root.rightChild)
    breadthfirst_comprension = [num for num in empty_bst.breadthfirst()]
    assert breadthfirst_comprension == [2, 1, 4, 3, 5]


def test_right_rotation_not_root(empty_bst):
    """Test left rotation on simple tree."""
    empty_bst.insert(5)
    empty_bst.insert(4)
    empty_bst.insert(3)
    empty_bst.right_rotation(empty_bst.root)
    breadthfirst_comprension = [num for num in empty_bst.breadthfirst()]
    assert breadthfirst_comprension == [4, 3, 5]
    empty_bst.insert(2)
    empty_bst.insert(1)
    empty_bst.right_rotation(empty_bst.root.leftChild)
    breadthfirst_comprension = [num for num in empty_bst.breadthfirst()]
    assert breadthfirst_comprension == [4, 2, 5, 1, 3]


# def test_right_rotation():
#     """Test right rotation."""
#     empty_bst.insert('Q')
#     empty_bst.insert('P')
#     empty_bst.insert('C')
#     empty_bst.insert('A')
#     empty_bst.insert('C')
#     empty_bst.rightChild(empty_bst.root.leftChild)
#     breadthfirst_comprension = [num for num in empty_bst.breadthfirst()]
#     assert breadthfirst_comprension == [4, 2, 5, 1, 3]

def test_insert_and_stuff(empty_bst):
    empty_bst.insert(1)
    empty_bst.insert(2)
    ls = empty_bst.insert(3)
    empty_bst.balance(ls)
