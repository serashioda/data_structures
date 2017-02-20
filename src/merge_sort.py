"""Merge Sort Module."""


def split_list(list):
    """Split the input list."""
    sub_lst = len(list) // 2
    return list[:sub_lst], list[sub_lst:]


def merge_sort(list):
    """Sorting method."""
    if len(list) < 2:
        return list
    l1, l2 = split_list(list)
    l1 = merge_sort(l1)
    l2 = merge_sort(l2)
    return merge(l1, l2)


def merge(a, b):
    """Helper method for merge_sort."""
    c = []
    while a and b:
        if a[0] > b[0]:
            c.append(b[0])
            del b[0]
        else:
            c.append(a[0])
            del a[0]
    while a:
        c.append(a[0])
        del a[0]
    while b:
        c.append(b[0])
        del b[0]
    return c


if __name__ == '__main__':  # pragma: no cover
    import timeit
    import random

    a = [random.randint(0, 21) for x in range(0, 21)]

    insertion = timeit.timeit(
        stmt='merge_sort(' + str(a) + ')',
        setup='from __main__ import merge_sort',
        number=1000,
    )
    print('The average time for merge_sort after 1000 times random: ' + str(insertion))
