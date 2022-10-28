import pytest
import numpy as np


def bellman_ford_basic(adjacents, n, k):
    dp = np.ones(shape=[n, n], dtype=np.float32) * np.inf
    dp[:, k] = 0.0

    for t in range(1, n):
        for i, j, d in adjacents:
            i = int(i)
            j = int(j)

            dp[t][j] = min(dp[t][j], min(dp[t - 1][j], dp[t - 1][i] + d))
    shortest = dp[n - 1, :]
    return shortest


def bellman_ford_previous(adjacents, n, k):
    last = np.ones(shape=[n], dtype=np.float32) * np.inf
    last[k] = 0.0

    for _ in range(n - 1):
        now = np.ones(shape=[n], dtype=np.float32) * np.inf

        for i, j, d in adjacents:
            i = int(i)
            j = int(j)

            now[j] = min(now[j], min(last[j], last[i] + d))
        now[k] = 0.0

        if np.allclose(last, now, atol=1e-6):
            break

        last = now
    return now


def bellman_ford_update(adjacents, n, k):
    queue = [k]

    visited = np.zeros(shape=[n], dtype=bool)
    visited[k] = True

    shortest = np.ones(shape=[n], dtype=np.float32) * np.inf
    shortest[k] = 0.0

    while len(queue) > 0:
        x = queue.pop(0)
        visited[x] = False

        for i, j, d in adjacents:
            i = int(i)
            j = int(j)

            if x != i:
                continue

            if not visited[j] and shortest[j] > shortest[i] + d:
                shortest[j] = shortest[i] + d

                queue.append(j)
                visited[j] = True
    return shortest


def test_bellman_ford_shortest_path():
    adjacents = np.array([
        [0, 1, 100.0],
        [0, 2, 500.0],
        [0, 3, 200.0],
        [1, 2, 100.0],
        [2, 3, 100.0],
        [3, 1, -150.0],
    ],
                         dtype=np.float32)
    n = 4
    k = 0

    ground = np.array([0.0, 50.0, 150.0, 200.0], dtype=np.float32)

    basic = bellman_ford_basic(adjacents, n, k)
    assert np.allclose(ground, basic, atol=1e-6), \
        'shortest distances mismatch between bellman-ford (basic) and groundtruth!'

    previous = bellman_ford_previous(adjacents, n, k)
    assert np.allclose(ground, previous, atol=1e-6), \
        'shortest distances mismatch between bellman-ford (previous) and groundtruth!'

    update = bellman_ford_update(adjacents, n, k)
    np.allclose(ground, update, atol=1e-6), \
        'shortest distances mismatch between bellman-ford (update) and groundtruth!'


def main():
    test_bellman_ford_shortest_path()


if __name__ == '__main__':
    main()