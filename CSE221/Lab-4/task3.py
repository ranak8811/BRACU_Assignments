inp = open('input3.txt', 'r')
out = open('output3.txt', 'w')

n, m = map(int, inp.readline().strip().split())

graph = {}
for i in range(1, n+1):
    graph[i] = []

for _ in range(m):
    u, v = map(int, inp.readline().strip().split())
    graph[u].append(v)
    graph[v].append(u)

print(graph)

def colourInitializing(graph):
    colours = {}
    for vertex in graph.keys():
        colours[vertex] = 0
    return colours

def DFS(graph, u, colours):
    colours[u] = 1
    path.append(u)
    for v in graph[u]:
        if colours[v] == 0:
            DFS(graph, v, colours)

colours = colourInitializing(graph)
print(colours)
path = []
DFS(graph, 1, colours)

path_str = ' '.join(str(v) for v in path)

out.write(path_str)

inp.close()
out.close()