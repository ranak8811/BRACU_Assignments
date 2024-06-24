import random
input_file = open(input_file.txt", "r")


# 1. The transaction register (using array)
N = int(input_file.readline())

register = [0]*N

for i in range(N):
  transaction = input_file.readline().split()
  if transaction[0] == 'l':
    register[i] = -int(transaction[1])
  elif transaction[0] == 'd':
    register[i] = int(transaction[1])

# print("Register:", register)

# 2. Fitness function
def instanceFitness(sequence:str, register = register):
  sum = 0
  for i in range(len(sequence)):
    if sequence[i] == '1':
      sum += register[i]
  return abs(sum)

# sec = "1111000"
# print(f"Fitness [{sec}]:", instanceFitness(sec))

# 3. Crossover function (child creator)
def crossover(population):
  # cross over between the fittest parents in the population
  new_population = []
  new_population_count = 0
  length = len(population)
  half_length = length//2

  j = 1
  while j < length:
    i = 0
    while i < j:
      # crossover between population[i][1] and population[j][1]
      # Child1
      child1 = population[i][1][:half_length] + population[j][1][half_length:]
      child1 = mutate(child1)
      new_population.append((instanceFitness(child1), child1))
      new_population_count += 1
      if new_population_count == length:
        return new_population
      
      # Child2
      child2 = population[j][1][:half_length] + population[i][1][half_length:]
      child2 = mutate(child2)
      new_population.append((instanceFitness(child2), child2))
      new_population_count += 1
      if new_population_count == length:
        return new_population

      i += 1      
    j += 1


# 4. Mutation function
def mutate(sequence:str):
  mutated_sequence = ''
  while '1' not in mutated_sequence: # if eg. 00000 is produced it will re-run the mutation 
    i = random.randint(0, len(sequence)-1)
    if sequence[i] == '0':
      mutated_sequence = sequence[:i]+'1'+sequence[i+1:]
    elif sequence[i] == '1':
      mutated_sequence = sequence[:i]+'0'+sequence[i+1:]
  return mutated_sequence

# 5. Random population generator
def generatePopulation(size:int, length = N):
  population = []
  while len(population) < size:
    member = ""
    for j in range(length):
      member += str(random.randint(0,1))
    
    if '1' in member: #to avoid all 0s. eg. '00000'
      population.append((instanceFitness(member) ,member))
  return population


# 6 Genetic algorithm
def geneticAlgorithm(register, POPULATION_SIZE = 10, MAX_GENERATIONS = 10):
  # Generate a random population
  population = generatePopulation(POPULATION_SIZE)
  ## Goal test on the generated parents
  population.sort(key = lambda x: x[0])
  # print("Parents:", population)
  if population[0][0] == 0:
    return population[0][1]

  # Crossover between the fittest pairs to generate a new generation of equal size
  for i in range(MAX_GENERATIONS):
    population = crossover(population)
    population.sort(key = lambda x: x[0])
    # print(population)
    if population[0][0] == 0:
      return population[0][1]
  return -1
    

# DRIVER CODE
print(geneticAlgorithm(register, 10, 50))

input_file.close()