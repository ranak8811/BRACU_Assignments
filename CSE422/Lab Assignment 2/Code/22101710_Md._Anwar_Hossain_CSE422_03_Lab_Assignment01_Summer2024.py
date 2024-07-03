import random

input_file = 'input.txt'
output_file = 'output.txt'

candidate_count = 10
max_generations = 100
variation_probability = 0.01

def generate_population(course_nums, timeslot_nums, candidate_count):
    population = []
    len_chromosome = course_nums * timeslot_nums
    for _ in range(candidate_count):
        chromosome = ''
        for i in range(len_chromosome):
            chromosome += random.choice('01')
        population.append(chromosome)

    return population

def fitness_calculation(chromosome, course_nums, timeslot_nums):
    overlap_penalty = 0
    consistency_penalty = 0

    class_schedule = []
    for i in range(timeslot_nums):
        timeslot = chromosome[i*course_nums: (i+1)*course_nums]
        class_schedule.append([int(bit) for bit in timeslot])
    
    # print(class_schedule)

    for timeslot in class_schedule:
        course_schedule_nums = sum(timeslot)
        if course_schedule_nums > 1:
            overlap_penalty += (course_schedule_nums - 1)

    # print(overlap_penalty)

    for x in range(course_nums):
        time_schedule_nums = sum(timeslot[x] for timeslot in class_schedule)
        if time_schedule_nums != 1:
            consistency_penalty += abs(time_schedule_nums - 1)

    # print(consistency_penalty)

    total_penalty = overlap_penalty + consistency_penalty
    fitness = -total_penalty

    # print(fitness)

    return fitness

def parents_selection(population, all_fitness):
    lowest_fitness = min(all_fitness)
    if lowest_fitness < 0:
        all_fitness = [fitness - lowest_fitness for fitness in all_fitness]
    
    # print(all_fitness)

    if sum(all_fitness) == 0:
        return random.sample(population, 2)
    
    parents = random.choices(population, weights=all_fitness, k=2)

    # print(parents)

    return parents

def crossover_method(p1, p2):
    crossing_point = random.randint(1, len(p1)-1)
    c1 = p1[:crossing_point] + p2[crossing_point:]
    c2 = p2[:crossing_point] + p1[crossing_point:]
    return c1, c2

# two point crossover methods for part 2
def two_point_crossover(p1, p2):
    point1 = random.randint(1, len(p1) - 2)
    point2 = random.randint(point1 + 1, len(p1) - 1)
    c1 = p1[:point1] + p2[point1:point2] + p1[point2:]
    c2 = p2[:point1] + p1[point1:point2] + p2[point2:]
    return c1, c2

def mutation_function(chromosome, variation_probability):

    # print(chromosome)

    mutated_chromosome = ''
    for bit in chromosome:
        if random.random() > variation_probability:
            mutated_chromosome += bit
        else:
            if bit == '0':
                mutated_chromosome += '1'
            else:
                mutated_chromosome += '0'

    return mutated_chromosome

def Genetic_Algorithm(course_nums, timeslot_nums, candidate_count, max_generations, variation_probability):
    population = generate_population(course_nums, timeslot_nums, candidate_count)
    best_chromosome = None
    best_fitness = float('-inf')

    for _ in range(max_generations):
        all_fitness = []
        for chromosome in population:
            all_fitness.append(fitness_calculation(chromosome, course_nums, timeslot_nums))
    
        # print(all_fitness)

        if max(all_fitness) > best_fitness:
            best_fitness = max(all_fitness)
            best_chromosome = population[all_fitness.index(best_fitness)]

        diverse_population = []
        for _ in range(candidate_count // 2):
            p1, p2 = parents_selection(population, all_fitness)
            c1, c2 = crossover_method(p1,p2)

            # c1, c2 = two_point_crossover(p1, p2)  # this one for part 2
            
            # print(c1,c2)
            diverse_population.extend([mutation_function(c1,variation_probability), mutation_function(c2, variation_probability)])

        population = diverse_population

    return best_chromosome, best_fitness

def input_reading(input_file):
    with open(input_file, 'r') as input:
        rows = input.readlines()
        course_nums, timeslot_nums = map(int, rows[0].strip().split())
        course_names = [row.strip() for row in rows[1:]]

        # print(course_names)

    return course_nums, timeslot_nums, course_names

def output_writing(output_file, best_chromosome, best_fitness, course_names, timeslot_nums):
    with open(output_file, 'w') as output:
        output.write(f"Best Schedule: {best_chromosome}\n")
        output.write(f"Fitness Value: {best_fitness}\n")

course_nums, timeslot_nums, course_names = input_reading(input_file)

best_schedule, best_fitness = Genetic_Algorithm(course_nums, timeslot_nums, candidate_count, max_generations, variation_probability)

output_writing(output_file, best_schedule, best_fitness, course_names, timeslot_nums)