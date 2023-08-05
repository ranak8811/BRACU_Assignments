inp = open('input3.txt', 'r')
out = open('output3.txt', 'w')

N, M = map(int, inp.readline().split())
graph = {i: [] for i in range(1, N + 1)}
for _ in range(M):
    u, v = map(int, inp.readline().split())
    graph[u].append(v)

def dfs_stack(graph, vertex, visited, stack):
    visited[vertex] = True
    for neighbor in graph[vertex]:
        if not visited[neighbor]:
            dfs_stack(graph, neighbor, visited, stack)
    stack.append(vertex)

def fill_stack(graph, n):
    stack = []
    visited = [False] * (n + 1)
    for vertex in range(1, n + 1):
        if not visited[vertex]:
            dfs_stack(graph, vertex, visited, stack)
    return stack

def dfs_scc(graph, vertex, visited, scc):
    visited[vertex] = True
    scc.append(vertex)
    for neighbor in graph[vertex]:
        if not visited[neighbor]:
            dfs_scc(graph, neighbor, visited, scc)

def find_scc(graph, n, stack):
    scc_list = []
    visited = [False] * (n + 1)
    while stack:
        vertex = stack.pop()
        if not visited[vertex]:
            scc = []
            dfs_scc(graph, vertex, visited, scc)
            scc_list.append(scc)
    return scc_list

stack = fill_stack(graph, N)
transposed_graph = {i: [] for i in range(1, N + 1)}
for u in graph:
    for v in graph[u]:
        transposed_graph[v].append(u)

scc_components = find_scc(transposed_graph, N, stack)

for scc in scc_components:
    out.write(" ".join(map(str, scc)) + "\n")

inp.close()
out.close()