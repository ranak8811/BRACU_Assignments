inp = open('input4.txt', 'r')
out = open('output4.txt', 'w')

n, m = map(int, inp.readline().strip().split())

graph = {}
for i in range(1, n+1):
    graph[i] = []

for _ in range(m):
    u, v = map(int, inp.readline().strip().split())
    graph[u].append(v)

def isCyclick(graph, v, visited, stack):
    visited[v] = True
    stack[v] = True

    for neighbor in graph[v]:
        if not visited[neighbor]:
            if isCyclick(graph, neighbor, visited, stack):
                return True
        elif stack[neighbor]:
                return True
            
    stack[v] = False
    return False

def hasCycle(graph):
    visited = [False] * (n+1)
    stack = [False] * (n+1)

    for v in graph.keys():
        if not visited[v]:
            if isCyclick(graph, v, visited, stack):
                return True
    return False

result = "YES" if hasCycle(graph) else "NO"
out.write(result)


inp.close()
out.close()