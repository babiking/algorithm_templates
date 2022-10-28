from array import array
import pytest
import copy
import random


def merge_sort(array):
    buffer = copy.deepcopy(array)

    size = len(array)

    merge_sort_recursion(array, buffer, 0, size - 1, level=0)
    return array


def merge_sort_recursion(array, buffer, left, right, level=0):
    if left == right:
        return

    middle = (left + right) // 2
    merge_sort_recursion(array, buffer, left, middle, level + 1)
    merge_sort_recursion(array, buffer, middle + 1, right, level + 1)
    merge_two_sorted_array(array, buffer, left, right)


def merge_two_sorted_array(array, buffer, left, right):
    middle = (left + right) // 2

    i = left
    j = middle + 1
    k = left

    while i <= middle and j <= right:
        if array[i] <= array[j]:
            buffer[k] = array[i]
            i += 1
            k += 1
        else:
            buffer[k] = array[j]
            j += 1
            k += 1

    while i <= middle:
        buffer[k] = array[i]
        i += 1
        k += 1

    while j <= right:
        buffer[k] = array[j]
        j += 1
        k += 1

    array[left:right + 1] = buffer[left:right + 1]


def test_merge_sort():
    n = 100
    array = [i for i in range(n)]
    random.shuffle(array)

    sort_array = merge_sort(copy.deepcopy(array))
    assert sort_array == sorted(array), \
        f'incorrected merge sorted array: {sort_array}!'


def main():
    test_merge_sort()


if __name__ == '__main__':
    main()
