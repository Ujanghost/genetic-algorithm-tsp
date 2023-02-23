import random

# define the distance matrix
distances = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

# define the parameters for the genetic algorithm
POPULATION_SIZE = 100
NUM_GENERATIONS = 1000
MUTATION_RATE = 0.01

# define a function to calculate the fitness of a solution
def calculate_fitness(solution):
    total_distance = 0
    for i in range(len(solution) - 1):
        total_distance += distances[solution[i]][solution[i+1]]
    total_distance += distances[solution[-1]][solution[0]]
    return 1 / total_distance

# define a function to create an initial population
def create_initial_population(num_cities):
    population = []
    for i in range(POPULATION_SIZE):
        individual = list(range(num_cities))
        random.shuffle(individual)
        population.append(individual)
    return population

# define a function to select parents for crossover
def select_parents(population):
    fitnesses = [calculate_fitness(individual) for individual in population]
    total_fitness = sum(fitnesses)
    probabilities = [fitness / total_fitness for fitness in fitnesses]
    parents = []
    for i in range(2):
        r = random.random()
        cumulative_probability = 0
        for j in range(len(population)):
            cumulative_probability += probabilities[j]
            if cumulative_probability >= r:
                parents.append(population[j])
                break
    return parents

# define a function to perform crossover
def crossover(parents):
    child = [-1] * len(parents[0])
    start = random.randint(0, len(parents[0]) - 1)
    end = random.randint(0, len(parents[0]) - 1)
    if start > end:
        start, end = end, start
    for i in range(start, end+1):
        child[i] = parents[0][i]
    j = 0
    for i in range(len(child)):
        if child[i] == -1:
            while parents[1][j] in child:
                j += 1
            child[i] = parents[1][j]
            j += 1
    return child

# define a function to perform mutation
def mutate(individual):
    if random.random() < MUTATION_RATE:
        i = random.randint(0, len(individual) - 1)
        j = random.randint(0, len(individual) - 1)
        individual[i], individual[j] = individual[j], individual[i]
    return individual

# create an initial population
population = create_initial_population(len(distances))

# evolve the population
for generation in range(NUM_GENERATIONS):
    # select parents for crossover
    parents = select_parents(population)
    # perform crossover
    child = crossover(parents)
    # mutate the child
    child = mutate(child)
    # replace a random individual in the population with the child
    population[random.randint(0, len(population) - 1)] = child

# find the best solution
best_individual = population[0]
best_fitness = calculate_fitness(best_individual)
for individual in population:
    fitness = calculate_fitness(individual)
    if fitness > best_fitness:
        best_individual = individual
        best_fitness = fitness

# print the best solution and its fitness
print("Best solution:", best_individual)
