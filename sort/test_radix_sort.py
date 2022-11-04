import pytest
import copy
import random
import numpy as np


def radix_sort(array):
    n = get_digital_length(np.max(np.abs(array)))

    size = len(array)

    dev = 1
    for _ in range(n):
        radices = [\
            array[i] // dev % 10 if array[i] >= 0 else int(array[i] / dev) % -10 \
                for i in range(size)]

        sorts = count_argsort(radices)

        array = [array[i] for i in sorts]

        dev *= 10
    return array


def get_digital_length(x):
    d = 0
    while (x != 0):
        d += 1
        x //= 10
    return d


def count_argsort(digits):
    size = len(digits)
    # range [-9, 9] mapping to [0, 18]
    counts = np.zeros(shape=[19], dtype=int)
    for digit in digits:
        counts[digit + 9] += 1

    for radix in range(1, 19):
        counts[radix] += counts[radix - 1]

    sorts = np.zeros(shape=[size], dtype=int)
    for i in range(size - 1, -1, -1):
        digit = digits[i]
        sorts[counts[digit + 9] - 1] = i
        counts[digit + 9] -= 1
    return sorts


def test_radix_sort():
    n = 10000
    array = [i - 3000 for i in range(n)]
    random.shuffle(array)

    sort_array = radix_sort(copy.deepcopy(array))
    assert sort_array == sorted(array), \
        f'incorrected quick sorted array: {sort_array}!'


def main():
    test_radix_sort()


if __name__ == '__main__':
    main()