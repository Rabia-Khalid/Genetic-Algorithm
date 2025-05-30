"""
Items:

(Weight, Value) Pairs: [(2, 3), (2, 7), (4, 2), (5, 9), (3, 5), (6, 12), (1, 4), (8, 13)]

Maximum Weight Capacity: 15

Expected Output:

The best combination of items (represented as a binary vector).

The total value of the best combination.
"""


import random

# Define the items (weight, value)
items = [(2, 3), (2, 7), (4, 2), (5, 9), (3, 5), (6, 12), (1, 4), (8, 13)]
max_weight = 15

# Genetic Algorithm parameters
population_size = 50
num_generations = 100
mutation_rate = 0.1
tournament_size = 5

# Generate a random individual (solution)
def create_individual():
    """
    Generate a random individual (solution).

    Returns:
        list: A list representing a solution where each element is 0 or 1.
              1 means the item is included in the knapsack, 0 means it is not.
    """
    return [random.randint(0, 1) for _ in range(len(items))]

# Generate initial population
def initial_population(population_size):
    """
    Generate the initial population of solutions.

    Parameters:
        population_size (int): The number of individuals in the population.

    Returns:
        list: A list of individuals representing the initial population.
    """
    individuals = []
    for i in range(population_size):
      new_individual = create_individual()
      individuals.append(new_individual)
    return individuals

# Calculate the fitness of an individual
def fitness(individual):
    """
    Calculate the fitness of an individual.

    The fitness is the total value of the items in the knapsack if the total weight
    does not exceed the maximum weight. Otherwise, the fitness is 0.

    Parameters:
        individual (list): A list representing an individual solution.

    Returns:
        int: The fitness value of the individual.
    """
    total_value = 0
    total_weight = 0
    fitness_value = 0
    for i, item in enumerate(individual):
        if item == 1:
          weight, value = items[i]
          total_value = total_value + value
          total_weight = total_weight + weight

          if total_weight > max_weight:
             return 0

          else:
            fitness_value = total_value

    return fitness_value





# Tournament selection
def tournament_selection(population):
    """
    Select an individual from the population using tournament selection.

    Parameters:
        population (list): A list of individuals representing the population.

    Returns:
        list: The fittest individual selected from the tournament.
    """
    tournament = random.sample(population, tournament_size)
    tournament_fitness = [fitness(individual) for individual in tournament]
    return tournament[tournament_fitness.index(max(tournament_fitness))]

# Crossover (single-point crossover)
def crossover(parent1, parent2):
    """
    Perform single-point crossover on two parents to produce two offspring.

    Parameters:
        parent1 (list): The first parent individual.
        parent2 (list): The second parent individual.

    Returns:
        tuple: Two offspring individuals produced by crossover.
    """
    crossover_point = random.randint(1, 7)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[: crossover_point] + parent1[ crossover_point:]
    offsprings = (child1, child2)
    return offsprings

# Mutation (flip mutation)
def mutate(individual):
    """
    Mutate an individual by flipping each bit with a certain probability.

    Parameters:
        individual (list): The individual to be mutated.

    Returns:
        list: The mutated individual.
    """
    if random.random() < mutation_rate:
       flip_index = random.randint(0, 7)
       individual[flip_index] = 1 - individual[flip_index]
    return individual


# Create the next generation
def next_generation(current_population):
    """
    Create the next generation of the population.

    Parameters:
        current_population (list): A list of individuals representing the current population.

    Returns:
        list: A list of individuals representing the new population.
    """
    new_population = []
    while len(new_population) < population_size:
        parent1 = tournament_selection(current_population)
        parent2 = tournament_selection(current_population)
        child_1, child_2 = crossover(parent1, parent2)
        child_1 = mutate(child_1)
        child_2 = mutate(child_2)
        new_population.extend([child_1, child_2])
    return new_population



# Initial population
current_population = initial_population(population_size)

# Evolve the population over multiple generations
for generation in range(num_generations):
    current_population = next_generation(current_population)

# Find the best solution in the final population
best_individual = max(current_population, key=fitness)
best_fitness = fitness(best_individual)

# Output the best solution and its value
print("Best individual:", best_individual)
print("Total value:", best_fitness)
