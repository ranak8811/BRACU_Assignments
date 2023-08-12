import heapq
inp = open('input3.txt', 'r')
out = open('output3.txt', 'w')


def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            danger_level = max(current_distance, weight)
            if danger_level < distances[neighbor]:
                distances[neighbor] = danger_level
                heapq.heappush(priority_queue, (danger_level, neighbor))

    return distances


N, M = map(int, inp.readline().split())
graph = {i: {} for i in range(1, N + 1)}
for _ in range(M):
    u, v, w = map(int, inp.readline().split())
    graph[u][v] = w

min_danger_level = dijkstra(graph, 1)[N]

if min_danger_level == float('inf'):
    out.write("Impossible")
else:
    out.write(str(min_danger_level))

inp.close()
out.close()
