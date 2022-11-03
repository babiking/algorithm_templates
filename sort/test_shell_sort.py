import pytest
import copy
import random


def shell_sort(array):
    size = len(array)

    gap = size // 2

    while gap > 0:
        for j in range(size):
            num = array[j]

            i = j - gap

            while i >= 0 and num < array[i]:
                array[i + gap] = array[i]

                i -= gap
            array[i + gap] = num

        gap //= 2
    return array


def test_shell_sort():
    n = 100
    array = [i for i in range(n)]
    random.shuffle(array)

    sort_array = shell_sort(copy.deepcopy(array))
    assert sort_array == sorted(array), \
        f'incorrected quick sorted array: {sort_array}!'


def main():
    test_shell_sort()


if __name__ == '__main__':
    main()