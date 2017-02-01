"""Quick Sort Implementation."""


def quick_sort(unsorted_list):
    """Quick sort method."""
    equal = []
    less = []
    greater = []

    if len(unsorted_list) > 1:
        pivot = unsorted_list[0]
        for x in unsorted_list:
            if x > pivot:
                greater.append(x)


if __name__ == '__main__':  # pragma: no cover
    import timeit
    import random

    a = [random.randint(0, 21) for x in range(0, 21)]

    insertion = timeit.timeit(
        stmt='quick_sort(' + str(a) + ')',
        setup='from __main__ import quick_sort',
        number=1000,
    )
    print("""
The average time for quick_sort after 1000 times random:
\n""" + str(insertion))
