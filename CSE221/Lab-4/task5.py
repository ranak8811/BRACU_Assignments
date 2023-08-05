from collections import deque

inp = open('input5.txt', 'r')
out = open('output5.txt', 'w')

n, m, d = map(int, inp.readline().strip().split())

graph = {}
for i in range(1, n+1):
    graph[i] = []

for _ in range(m):
    u, v = map(int, inp.readline().strip().split())
    graph[u].append(v)
    graph[v].append(u)

def BFS(G, start, destination):
    visited = [False] * (n+1)
    distance = [float('inf')] * (n+1)
    parent = [None] * (n+1)

    queue = deque()
    queue.append(start)
    visited[start] = True
    distance[start] = 0

    while queue:
        current = queue.popleft()

        if current == destination:
            break

        for neighbor in G[current]:
            if not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = True
                distance[neighbor] = distance[current] + 1
                parent[neighbor] = current

    path = []
    node = destination
    while node is not None:
        path.append(node)
        node = parent[node]
    path.reverse()

    return distance[destination], path

shortest_distance, shortest_path = BFS(graph, 1, d)

# print(shortest_distance)
out.write(f"Time: {str(shortest_distance)}" + '\n')

path_str = ' '.join(str(node) for node in shortest_path)
# print(path_str)
out.write(f"Shortest Path: {path_str}")

inp.close()
out.close()