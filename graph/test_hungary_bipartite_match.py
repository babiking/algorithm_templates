import pytest
import numpy as np


def hungary_bipartite_match(adjacents):
    ni, nj = adjacents.shape

    visited = np.zeros(shape=[nj], dtype=bool)
    matched = -1 * np.ones(shape=[nj], dtype=np.int32)

    for i in range(ni):
        hungray_bipartite_match_recursive(i, adjacents, visited, matched)

    matches = [(i, j) for j, i in enumerate(matched) if i >= 0]
    return matches


def hungray_bipartite_match_recursive(i, adjacents, visited, matched):
    ni, nj = adjacents.shape

    for j in range(nj):
        if adjacents[i][j] and not visited[j]:
            visited[j] = True

            if matched[j] < 0 or \
                hungray_bipartite_match_recursive(matched[j], adjacents, visited, matched):
                matched[j] = i
                return True
    return False


def test_hungary_bipartite_match():
    # build
    links = [
        (0, 1),
        (0, 3),
        (1, 1),
        (2, 0),
        (2, 2),
        (3, 3),
    ]
    xs, ys = zip(*links)
    adjacents = np.zeros(shape=[max(xs) + 1, max(ys) + 1], dtype=bool)
    adjacents[xs, ys] = True

    matches = hungary_bipartite_match(adjacents)

    assert len(matches) == 3, 'incorrect hungary bipartite match number!'


def main():
    test_hungary_bipartite_match()


if __name__ == '__main__':
    main()