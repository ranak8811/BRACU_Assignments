import heapq
inp = open('input1.txt', 'r')
out = open('output1.txt', 'w')


def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


N, M = map(int, inp.readline().split())
graph = {i: {} for i in range(1, N + 1)}
for _ in range(M):
    u, v, w = map(int, inp.readline().split())
    graph[u][v] = w
S = int(inp.readline())

shortest_distances = dijkstra(graph, S)

for distance in shortest_distances.values():
    out.write(str(distance if distance < float('infinity') else -1) + " ")

inp.close()
out.close()
