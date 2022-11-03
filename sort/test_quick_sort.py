import pytest
import copy
import random


def quick_sort(array):
    quick_sort_recursion(array, 0, len(array) - 1, level=0)
    return array


def quick_sort_recursion(array, left, right, level=0):
    if left >= right:
        return

    middle = partition_double_pointer(array, left, right)

    quick_sort_recursion(array, left, middle - 1, level + 1)
    quick_sort_recursion(array, middle + 1, right, level + 1)


def swap(array, i, j):
    tmp = array[i]
    array[i] = array[j]
    array[j] = tmp


def partition_double_pointer(array, start, end):
    pivot = array[start]

    left = start + 1
    right = end

    while left < right:
        while left < right and array[left] < pivot:
            left += 1
        
        if left != right:
            swap(array, left, right)
            right -= 1
    
    if left == right and array[right] > pivot:
        right -= 1
    
    if right != start:
        swap(array, start, right)
    return right


def test_quick_sort():
    n = 100
    array = [i for i in range(n)]
    random.shuffle(array)

    sort_array = quick_sort(copy.deepcopy(array))
    assert sort_array == sorted(array), \
        f'incorrected quick sorted array: {sort_array}!'


def main():
    test_quick_sort()


if __name__ == '__main__':
    main()
