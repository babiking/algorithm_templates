import pytest
import copy
import random


class HeapSorter(object):

    def __init__(self, array=None, compare=None):
        self.array = copy.deepcopy(array) if isinstance(array, list) else []
        self.compare = HeapSorter.greater if compare is None else compare

        if self.__len__() > 0:
            self.build()

    def up(self, i):
        while (i - 1) // 2 >= 0 \
            and self.compare(self.array[i], self.array[(i - 1) // 2]):
            HeapSorter.swap(self.array, i, (i - 1) // 2)

            i = (i - 1) // 2

    def down(self, i, size):
        l = i * 2 + 1
        r = i * 2 + 2

        m = i
        if l < size and self.compare(self.array[l], self.array[m]):
            m = l

        if r < size and self.compare(self.array[r], self.array[m]):
            m = r

        if m != i:
            HeapSorter.swap(self.array, m, i)

            self.down(m, size)

    def get(self, i):
        if i < 0 or i >= self.__len__():
            return
        return self.array[i]

    def push(self, x):
        self.array.append(x)

        self.up(self.__len__() - 1)

    def pop(self):
        if self.empty():
            return

        v = self.array[0]

        self.array[0] = self.array[self.__len__() - 1]
        self.array.pop(-1)

        self.down(0, self.__len__())
        return v

    def build(self):
        i = self.__len__() // 2 - 1
        while i >= 0:
            self.down(i, self.__len__())
            i -= 1

    def empty(self):
        return self.__len__() == 0

    def __len__(self):
        return len(self.array)

    @staticmethod
    def greater(x, y):
        return x > y

    @staticmethod
    def swap(array, i, j):
        tmp = array[i]
        array[i] = array[j]
        array[j] = tmp


def test_heap_sorter():
    n = 100
    array = [i for i in range(n)]
    random.shuffle(array)

    min_heap_sorter = HeapSorter(array, compare=lambda x, y: x < y)
    sort_array = []
    while not min_heap_sorter.empty():
        sort_array.append(min_heap_sorter.pop())
    assert sort_array == sorted(array), \
        f'incorrected max heap sorted array: {sort_array}!'

    min_heap_sorter = HeapSorter()
    for i in array:
        min_heap_sorter.push(i)
    sort_array = []
    while not min_heap_sorter.empty():
        sort_array.append(min_heap_sorter.pop())
    assert sort_array == sorted(array, reverse=True), \
        f'incorrected min heap sorted array: {sort_array}!'


def main():
    test_heap_sorter()


if __name__ == '__main__':
    main()