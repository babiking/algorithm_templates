import pytest
import numpy as np
from collections import namedtuple
from sort.test_heap_sort import HeapSorter


def convert_adjacents_to_distances(adjacents, n, directed=True):
    distances = np.ones(shape=[n, n], dtype=np.float32) * np.inf
    distances[range(n), range(n)] = 0.0
    for i, j, d in adjacents:
        distances[int(i)][int(j)] = d

        if not directed:
            distances[int(j)][int(i)] = d
    
    
    return distances


def dijkstra_by_traverse(adjacents, n, k):
    distances = convert_adjacents_to_distances(adjacents, n)

    shortest = np.ones(shape=[n], dtype=np.float32) * np.inf
    shortest[k] = 0.0

    visited = np.zeros(shape=[n], dtype=bool)

    for _ in range(n):
        x = -1
        for y in range(n):
            if (not visited[y]) and (x == -1 or shortest[y] < shortest[x]):
                x = y
        visited[x] = True

        for y in range(n):
            if not visited[y] and shortest[y] > distances[x][y] + shortest[x]:
                shortest[y] = distances[x][y] + shortest[x]
    return shortest


def dijkstra_by_heap_sort(adjacents, n, k):
    distances = convert_adjacents_to_distances(adjacents, n)

    shortest = np.ones(shape=[n], dtype=np.float32) * np.inf
    shortest[k] = 0.0

    DistanceTriplet = namedtuple('DistanceTriplet', ['i', 'j', 'distance'])

    heap_sorter = HeapSorter(compare=lambda x, y: x.distance < y.distance)
    heap_sorter.push(DistanceTriplet(k, k, 0.0))

    while not heap_sorter.empty():
        triplet = heap_sorter.pop()

        src = triplet.j

        for dst in range(n):
            if distances[src][dst] == np.inf:
                continue

            if shortest[dst] > shortest[src] + distances[src][dst]:
                shortest[dst] = shortest[src] + distances[src][dst]

                heap_sorter.push(
                    DistanceTriplet(
                        src,
                        dst,
                        distances[src][dst],
                    ))
    return shortest


def test_dijkstra_shortest_path():
    adjacents = np.array([
        [0, 1, 1.0],
        [0, 2, 1.0],
        [0, 3, 3.0],
        [1, 3, 2.0],
        [2, 3, 1.0],
        [1, 4, 1.0],
        [3, 4, 2.0],
    ],
                         dtype=np.float32)

    n = 5
    k = 0

    ground = np.array([0.0, 1.0, 1.0, 2.0, 2.0], dtype=np.float32)

    traverse = dijkstra_by_traverse(adjacents, n, k)
    assert [x == pytest.approx(y, 1e-6) for x, y in zip(traverse, ground)], \
        'shortest distances mismatch between dijkstra (traverse) and groundtruth!'
    
    heap_sort = dijkstra_by_heap_sort(adjacents, n, k)
    assert [x == pytest.approx(y, 1e-6) for x, y in zip(heap_sort, ground)], \
        'shortest distances mismatch between dijkstra (heap sort) and groundtruth!'


def main():
    test_dijkstra_shortest_path()


if __name__ == '__main__':
    main()
