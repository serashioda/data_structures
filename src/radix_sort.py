"""Radix Sort Implementation."""


def radix_sort(unsorted_lst):
    """Radix_sort."""
    max_num = max(unsorted_lst)
    passes = len(str(max_num))
    padded_lst = []
    buckets = [[] for x in range(0, 10)]
    while passes:
        for x in unsorted_lst:
            x = str(x).zfill(passes)
            buckets[int((x[passes - 1]))].append(x)

        unsorted_lst = put_back(bucket)
        buckets = [[] for x in range(0, 10)]
        passes -= 1
    return [int(x) for x in unsorted_lst]


def put_back(buckets):
    """Return buckets."""
    s = []
    for bucket in buckets:
        s.extend(bucket)
    return s
