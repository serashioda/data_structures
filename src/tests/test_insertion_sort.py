"""Testing module for Insertion Sort."""
import pytest

TEST_TABLE = [
    [[3, 2, 5], [2, 3, 5]],
    [[9, 4, 1, 7, 5, 2, 8, 3, 6], [1, 2, 3, 4, 5, 6, 7, 8, 9]],
    [['a', 'd', 'e', 'g', 'f', 'b', 'c'], ['a', 'b', 'c', 'd', 'e', 'f', 'g']]
]


@pytest.mark.parametrize("numbers, result", TEST_TABLE)
def test_insertion_sort(numbers, result):
    """Test the insertion sort function."""
    from insertion_sort import insertion_sort
    assert insertion_sort(numbers) == result