from queue import PriorityQueue

file = open('Input_file.txt', 'r')

# Code starts here

class Graph:
  def __init__(self, input_file):
    self.nodes = {}
    self._createGraph(input_file)

  def _createGraph(self, input_file):
    for line in input_file:
      line = line.strip().split()
      self.nodes[line[0]] = {"heuristic": int(line[1]), "explored": False, "distance_from_start": float("inf"), "parent": None, "neighbours": {line[i]: int(line[i+1]) for i in range(2, len(line), 2)}}

  def printGraph(self):
    for node in self.nodes:
      print(node, self.nodes[node])

  def _g(self, node:str):
    return self.nodes[node]["distance_from_start"]

  def _h(self, node:str):
    return self.nodes[node]["heuristic"]

  def _f(self, node:str):
    return self._g(node) + self._h(node)

  def _resetAStar(self):
    for node in self.nodes:
      self.nodes[node]["distance_from_start"] = float("inf")
      self.nodes[node]["explored"] = False
      self.nodes[node]["parent"] = None
    
# Code ends here

  def aStar(self, start, goal = "Bucharest"):
    self._resetAStar()
    self.nodes[start]["distance_from_start"] = 0
    pq = PriorityQueue()
    pq.put((self._f(start), start))

    while not pq.empty():
      parent = pq.get()[1]

      if parent == goal:
        break

      # if self.nodes[parent]["explored"]:
      #   continue
      
      self.nodes[parent]["explored"] = True

      for child in self.nodes[parent]["neighbours"]:
        if not self.nodes[child]["explored"]:
          distance = self.nodes[parent]["distance_from_start"] + self.nodes[parent]["neighbours"][child]
          if distance < self.nodes[child]["distance_from_start"]:
            self.nodes[child]["distance_from_start"] = distance
            self.nodes[child]["parent"] = parent
          pq.put((self._f(child), child))

    # Output
    if self.nodes[goal]["distance_from_start"] == float("inf"):
      print("NO PATH FOUND")
      return

    path = []
    current = goal
    while current:
      path.append(current)
      current = self.nodes[current]["parent"]

    path.reverse()
    print("Path:", end = " ")
    print(*path, sep=" -> ")
    print("Total distance:", self.nodes[goal]["distance_from_start"], "km")
    

# Driver code
## Create the graph
graph = Graph(file)

## Take input
print("Start node:", end = " ")
start_node = input()
print("Destination:", end = " ")
goal_node = input()

## Find the path
graph.aStar(start_node, goal_node)

file.close()