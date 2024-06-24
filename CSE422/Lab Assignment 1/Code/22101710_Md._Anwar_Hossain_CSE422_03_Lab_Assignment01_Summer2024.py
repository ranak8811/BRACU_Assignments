import heapq

def A_star_Search(graph, heuristics, start, end):
    nodes = [(0, start)]
    path = {}
    values = {position: float('inf') for position in graph}
    values[start] = 0

    while nodes:
        _, current_node = heapq.heappop(nodes)

        if current_node == end:
            path_sequence = restore_track(path, current_node)
            return path_sequence

        for adjacent_city, cost in graph[current_node]:
            probable_value = values[current_node] + cost
            if probable_value < values[adjacent_city]:
                path[adjacent_city] = current_node
                values[adjacent_city] = probable_value
                total_value = probable_value + heuristics[adjacent_city]
                heapq.heappush(nodes, (total_value, adjacent_city))
    
    return None

def restore_track(path, current_node):
    path_sequence = [current_node]
    while current_node in path:
        current_node = path[current_node]
        path_sequence.insert(0, current_node)
    return path_sequence

# Open files
with open('22101710_Md._Anwar_Hossain_CSE422_03_Lab_Assignment01_InputFile_Summer2024.txt', 'r') as f1, open('22101710_Md._Anwar_Hossain_CSE422_03_Lab_Assignment01_OutputFile_Summer2024.txt', 'w') as f2:
    all_lines = f1.readlines()

    graph = {}
    heuristics = {}

    for x in all_lines:
        pieces = x.split()
        position = pieces[0]
        heuristic = int(pieces[1])

        next_to = []
        for i in range(2, len(pieces), 2):
            city = pieces[i]
            distance = int(pieces[i + 1])
            next_to.append((city, distance))

        graph[position] = next_to
        heuristics[position] = heuristic

    # print(graph)
    # print('----------------------------------------------------------------')
    # print(heuristics)   

    start_position = input('Start node: ')
    end_position = input('Destination: ')

    path_sequence = A_star_Search(graph, heuristics, start_position, end_position)

    if path_sequence:
        total_distance = 0
        for i in range(len(path_sequence) - 1):
            current_position = path_sequence[i]
            next_position = path_sequence[i + 1]

            for adjacent_position, cost in graph[current_position]:
                if adjacent_position == next_position:
                    total_distance += cost
                    break

        f2.write("Path: " + " -> ".join(path_sequence) + "\n")
        f2.write(f"Total distance: {total_distance} km\n")
    else:
        f2.write(f"No path found from {start_position} to {end_position}\n")
