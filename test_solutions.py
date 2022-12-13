from solutions import *


def test_binary_search():
    assert binary_search([1, 2, 4, 6, 7, 8], 7) == 4
    assert binary_search([1, 2, 3, 4, 6, 7], 5) == -1


def test_topological_sort():
    case1 = {
        "connections": [[1, 0], [2, 0], [3, 1], [3, 2]],
        "n": 4,
        "expected": [3, 1, 2, 0],
    }
    assert topological_sort(case1["connections"], case1["n"]) == case1["expected"]


def test_back_tracking():
    assert back_tracking([1, 2, 3]) == [
        [1, 2, 3],
        [1, 3, 2],
        [2, 1, 3],
        [2, 3, 1],
        [3, 1, 2],
        [3, 2, 1],
    ]
