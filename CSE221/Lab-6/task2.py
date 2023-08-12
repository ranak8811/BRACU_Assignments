import heapq

inp = open('input2.txt', 'r')
out = open('output2.txt', 'w')

N, M = map(int, inp.readline().split())
graph = {i: {} for i in range(1, N + 1)}

for _ in range(M):
    u, v, w = map(int, inp.readline().split())
    graph[u][v] = w

S, T = map(int, inp.readline().split())

distances_S = {node: float('inf') for node in graph}
distances_S[S] = 0
pq_S = [(0, S)]

while pq_S:
    current_distance, current_vertex = heapq.heappop(pq_S)

    if current_distance > distances_S[current_vertex]:
        continue

    for neighbor, weight in graph[current_vertex].items():
        distance = current_distance + weight

        if distance < distances_S[neighbor]:
            distances_S[neighbor] = distance
            heapq.heappush(pq_S, (distance, neighbor))

distances_T = {node: float('inf') for node in graph}
distances_T[T] = 0
pq_T = [(0, T)]

while pq_T:
    current_distance, current_vertex = heapq.heappop(pq_T)

    if current_distance > distances_T[current_vertex]:
        continue

    for neighbor, weight in graph[current_vertex].items():
        distance = current_distance + weight

        if distance < distances_T[neighbor]:
            distances_T[neighbor] = distance
            heapq.heappush(pq_T, (distance, neighbor))

min_time = float('inf')
meeting_node = None

for node in range(1, N + 1):
    total_time = max(distances_S[node], distances_T[node])
    if total_time < min_time:
        min_time = total_time
        meeting_node = node

if min_time == float('inf') or meeting_node is None:
    out.write("Impossible")
else:
    out.write(f"Time {min_time}\nNode {meeting_node}")

inp.close()
out.close()
