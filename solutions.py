import collections
from typing import List


# >>> begin [basic-1] binary search
def binary_search(arr: List[int], target: int) -> int:
    """
    Perform binary search in a sorted array.

    params:
        - arr(list): a sorted list
        - target(int): a target number to look for

    returns:
        - an index of the target
    """
    start = 0
    end = len(arr)
    while start + 1 < end:
        mid = start + (end - start) // 2
        if target == arr[mid]:
            return mid
        elif target < arr[mid]:
            end = mid
        else:
            start = mid

    if arr[start] == target:
        return start
    if arr[end] == target:
        return end

    return -1


# <<< end [basic-1] binary search


# >>> start [basic-2] topological sorting
def topological_sort(connections: List[List[int]], n: int) -> List[int]:
    """
    Perform togological sorting given a graph.

    params:
        - connections(list): a list of connections between nodes
        - n(int) total number of nodes

    returns:
        - a list of togologically sorted nodes
    """
    adj = collections.defaultdict(list)
    indegree = collections.defaultdict(int)
    for c in connections:
        adj[c[0]].append(c[1])
        indegree[c[1]] += 1

    q = collections.deque()
    for i in range(n):
        if indegree[i] == 0:
            q.append(i)

    res = []
    while q:
        node = q.popleft()
        res.append(node)
        for nei in adj[node]:
            indegree[nei] -= 1
            if indegree[nei] == 0:
                q.append(nei)

    return res


# <<< end [basic-2] topological sorting


# >>> start [basic-3] back tracking
def back_tracking(arr: List[int]) -> List[List[int]]:
    res = []

    def dfs(temp: List[int], visited: set) -> None:
        if len(temp) == len(arr):
            res.append(temp[:])
            return

        for i in range(len(arr)):
            if i not in visited:
                visited.add(i)
                temp.append(arr[i])
                dfs(temp, visited)
                temp.pop()
                visited.remove(i)

    dfs([], set())
    return res
# <<< end [basic-3] back tracking


# >>> start [basic-4] union find
def union_find():
    pass
# >>> start [basic-4] union find

