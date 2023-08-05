inp = open('input7.txt', 'r')
out = open('output7.txt', 'w')

N = int(inp.readline())

graph = {}
for i in range(1, N+1):
    graph[i] = []

for _ in range(N-1):
    u, v = map(int, inp.readline().strip().split())
    graph[u].append(v)
    graph[v].append(u)

max_cities = 0
city_a = 0
city_b = 0

for city in graph:
    visited = set()
    stack = [(city, 0)]

    while stack:
        curr_city, num_cities = stack.pop()

        visited.add(curr_city)

        if num_cities > max_cities:
            max_cities = num_cities
            city_a = city
            city_b = curr_city

        for neighbor in graph[curr_city]:
            if neighbor not in visited:
                stack.append((neighbor, num_cities + 1))

out.write(str(city_a) + " " + str(city_b))

inp.close()
out.close()
