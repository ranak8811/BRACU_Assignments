# Using BFS

from collections import deque

inp = open('input2.txt', 'r')
out = open('output2.txt', 'w')

N, M = map(int, inp.readline().split())
prerequisites = [tuple(map(int, inp.readline().split())) for _ in range(M)]

def bfs_order(N, prerequisites):
    graph = {i: [] for i in range(1, N + 1)}
    in_degree = {i: 0 for i in range(1, N + 1)}
    for A, B in prerequisites:
        graph[A].append(B)
        in_degree[B] += 1

    queue = deque()
    for i in range(1, N + 1):
        if in_degree[i] == 0:
            queue.append(i)

    result = []
    while queue:
        course = min(queue)
        queue.remove(course)
        result.append(course)
        for neighbor in graph[course]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return result if len(result) == N else []

order_bfs = bfs_order(N, prerequisites)

out.write(" ".join(map(str, order_bfs)) if order_bfs else "IMPOSSIBLE")

inp.close()
out.close()