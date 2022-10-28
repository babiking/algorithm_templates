import pytest


def kahn_topology_sort(prerequisites, n):
    out_neighbors = [set() for _ in range(n)]
    in_degrees = [0 for _ in range(n)]
    for i, j in prerequisites:
        out_neighbors[i].add(j)
        in_degrees[j] += 1

    queue = []
    sorts = []
    visited = [False for _ in range(n)]
    for _ in range(n + 1):
        if len(queue) > 0:
            x = queue.pop(0)
            sorts.append(x)

            for y in out_neighbors[x]:
                in_degrees[y] -= 1

        for j, deg in enumerate(in_degrees):
            if not visited[j] and deg == 0:
                queue.append(j)
                visited[j] = True
    return sorts if in_degrees.count(0) == n else []


def test_kahn_topology_sort():
    prerequisites = [
        [0, 1],
        [0, 2],
        [1, 3],
        [2, 3],
    ]
    n = 4
    ground = [0, 1, 2, 3]
    kahn = kahn_topology_sort(prerequisites, n)
    assert all([x == y for x, y in zip(kahn, ground)]), \
        'topology sort mismatch between kahn and groundtruth!'

    prerequisites = [[0, 1], [1, 0]]
    n = 2
    kahn = kahn_topology_sort(prerequisites, n)
    assert len(kahn) == 0, 'loop topology can NOT be sorted!'


def main():
    test_kahn_topology_sort()


if __name__ == '__main__':
    main()