"""Tests for insertion_sort module."""
from insertion_sort import insertion_sort
import random

letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'


def test_sort_random_letters():
    """Test sort random letters."""
    for x in range(1, 3000):
        rand_letters = [random.choice(letters) for a in letters]
        python_sorted = sorted(rand_letters)
        insertion_sorted = insertion_sort(rand_letters)
        assert python_sorted == insertion_sorted


def test_sort_random_numbers():
    """Test sort random numbers."""
    for x in range(1, 3000):
        rand_numbers = [random.randint(1, 20) for a in range(1, 20)]
        python_sorted = sorted(rand_numbers)
        insertion_sorted = insertion_sort(rand_numbers)
        assert python_sorted == insertion_sorted


def test_sort_random_big_numbers():
    """Test sort big random numbers."""
    for x in range(1, 1000):
        rand_numbers = [random.randint(1, 20) for a in range(1, random.randint(200, 300))]
        python_sorted = sorted(rand_numbers)
        insertion_sorted = insertion_sort(rand_numbers)
        assert python_sorted == insertion_sorted
