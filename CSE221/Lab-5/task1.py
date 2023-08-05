# Using the DFS approach.

inp = open('input1.txt', 'r')
out = open('output1.txt', 'w')

N, M = map(int, inp.readline().split())
prerequisites = [tuple(map(int, inp.readline().split())) for _ in range(M)]

def dfs(course, graph, visited, stack, path):
    visited.add(course)
    path.add(course)

    for neighbor in graph[course]:
        if neighbor in path:
            return True
        if neighbor not in visited:
            if dfs(neighbor, graph, visited, stack, path):
                return True

    path.remove(course)
    stack.append(course)
    return False

def dfs_order(N, prerequisites):
    graph = {i: [] for i in range(1, N + 1)}
    for A, B in prerequisites:
        graph[A].append(B)
    
    visited = set()
    stack = []

    for i in range(1, N + 1):
        if i not in visited:
            if dfs(i, graph, visited, stack, set()):
                return []

    return stack[::-1] if len(stack) == N else []

order_dfs = dfs_order(N, prerequisites)

out.write(" ".join(map(str, order_dfs)) if order_dfs else "IMPOSSIBLE")

inp.close()
out.close()




#------------------------------------------------------------------------------


# Using the BFS approach.

# from collections import deque

# inp = open('input1.txt', 'r')
# out = open('output1.txt', 'w')


# N, M = map(int, inp.readline().split())
# prerequisites = [tuple(map(int, inp.readline().split())) for _ in range(M)]
# # print(prerequisites)


# def bfs_order(N, prerequisites):
#     graph = {i: [] for i in range(1, N + 1)}
#     in_degree = {i: 0 for i in range(1, N + 1)}
#     for A, B in prerequisites:
#         graph[A].append(B)
#         in_degree[B] += 1

#     # print(graph)
#     # print(in_degree)

#     queue = deque()
#     result = []
#     for i in range(1, N + 1):
#         if in_degree[i] == 0:
#             queue.append(i)
#     while queue:
#         course = queue.popleft()
#         result.append(course)
#         for neighbor in graph[course]:
#             in_degree[neighbor] -= 1
#             if in_degree[neighbor] == 0:
#                 queue.append(neighbor)
#     return result if len(result) == N else []

# order_bfs = bfs_order(N, prerequisites)

# out.write(" ".join(map(str, order_bfs)) if order_bfs else "IMPOSSIBLE")

# inp.close()
# out.close()