"""Implementation of insertion sort."""


def insertion_sort(numbers):
    """."""
    def find_op(idx, lst):
        return len(lst) - idx - 1
    for idx, num in enumerate(numbers):
        num_sorted = numbers[:idx]
        num_sorted = num_sorted[::-1]
        for idx_2, num_sort in enumerate(num_sorted):
            if num_sort > num:
                numbers[idx] = num_sort
                numbers[find_op(idx_2, num_sorted)] = num
                idx = find_op(idx_2, num_sorted)
    return numbers

if __name__ == '__main__':  # pragma: no cover
    import timeit
    import random

    a = [random.randint(0, 21) for x in range(0, 21)]

    insertion = timeit.timeit(
        stmt='insertion_sort(' + str(a) + ')',
        setup='from __main__ import insertion_sort',
        number=1000,
    )
    print('The average time for insertion_sort after 1000 times ran:' + str(insertion))
