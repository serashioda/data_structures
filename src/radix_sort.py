"""Radix Sort Implementation."""


def radix_sort(unsorted_lst):
    """Radix_sort."""
    max_num = max(unsorted_lst)
    passes = len(str(max_num))
    buckets = [[] for x in range(0, 10)]
    while passes:
        for x in unsorted_lst:
            x = str(x).zfill(passes)
            buckets[int((x[passes - 1]))].append(x)

        unsorted_lst = put_back(buckets)
        buckets = [[] for x in range(0, 10)]
        passes -= 1
    return [int(x) for x in unsorted_lst]


def put_back(buckets):
    """Return buckets."""
    s = []
    for bucket in buckets:
        s.extend(bucket)
    return s

if __name__ == '__main__':  # pragma: no cover
    import timeit
    import random

    a = [random.randint(0, 21) for x in range(0, 21)]

    insertion = timeit.timeit(
        stmt='radix_sort(' + str(a) + ')',
        setup='from __main__ import radix_sort',
        number=1000,
    )
    print('The average time for radix_sort after 1000 times random: ' + str(insertion))
