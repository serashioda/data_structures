"""Implementation of insertion sort."""


def insertion_sort(numbers):
    """."""
    def find_op(idx, lst):
        return len(lst) - idx - 1
    for idx, num in enumerate(numbers):
        print(numbers)
        num_sorted = numbers[:idx]
        num_sorted = num_sorted[::-1]
        print('Reversed rest of numbers: ', num_sorted)
        for idx_2, num_sort in enumerate(num_sorted):
            print("Num to sort: ", num_sort)
            if num_sort > num:
                print(numbers[idx], num_sort)
                numbers[idx] = num_sort
                print(numbers[find_op(idx_2, num_sorted)], num)
                numbers[find_op(idx_2, num_sorted)] = num
                idx = find_op(idx_2, num_sorted)
                print('Replace', numbers)
    return numbers
