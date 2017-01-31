"""Tests for merge_sort module."""
from merge_sort import merge_sort
import random

letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'


def test_sort_random_letters():
    """Test sort random letters."""
    for x in range(1, 3000):
        rand_letters = [random.choice(letters) for a in letters]
        python_sorted = sorted(rand_letters)
        merge_sorted = merge_sort(rand_letters)
        assert python_sorted == merge_sorted


def test_sort_random_numbers():
    """Test sort random numbers."""
    for x in range(1, 3000):
        rand_numbers = [random.randint(1, 20) for a in range(1, 20)]
        python_sorted = sorted(rand_numbers)
        merge_sorted = merge_sort(rand_numbers)
        assert python_sorted == merge_sorted
