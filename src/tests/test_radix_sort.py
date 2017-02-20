"""Tests for radix_sort module."""
from radix_sort import radix_sort
import random


def test_sort_random_numbers():
    """Test sort random numbers."""
    for x in range(1, 3000):
        rand_numbers = [random.randint(1, 20) for a in range(1, 20)]
        python_sorted = sorted(rand_numbers)
        radix_sorted = radix_sort(rand_numbers)
        assert python_sorted == radix_sorted
