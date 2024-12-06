import random

def initialize_population(pop_size, chromosome_length):
    return ["".join(random.choice("01") for _ in range(chromosome_length)) for _ in range(pop_size)]

def fitness_function(individual):
    return individual.count('1')

def roulette_wheel_selection(population, fitness_scores):
    total_fitness = sum(fitness_scores)
    probabilities = [f / total_fitness for f in fitness_scores]
    cumulative_probabilities = [sum(probabilities[:i + 1]) for i in range(len(probabilities))]
    pick = random.random()
    for idx, prob in enumerate(cumulative_probabilities):
        if pick <= prob:
            return population[idx]

def single_point_crossover(parent1, parent2):
    point = random.randint(1, len(parent1) - 1)
    return parent1[:point] + parent2[point:], parent2[:point] + parent1[point:]

def bit_flip_mutation(individual, mutation_rate=0.01):
    return "".join(bit if random.random() > mutation_rate else "1" if bit == "0" else "0" for bit in individual)

def genetic_algorithm(pop_size, chromosome_length, generations, mutation_rate=0.01):
    population = initialize_population(pop_size, chromosome_length)
    print(f"Initial Population: {population}\n")
    for gen in range(generations):
        fitness_scores = [fitness_function(ind) for ind in population]
        best_individual = max(population, key=fitness_function)
        best_fitness = fitness_function(best_individual)
        print(f"Generation {gen + 1}")
        print(f"Population: {population}")
        print(f"Fitness Scores: {fitness_scores}")
        print(f"Best Individual: {best_individual}, Fitness: {best_fitness}\n")
        new_population = []
        while len(new_population) < pop_size:
            parent1 = roulette_wheel_selection(population, fitness_scores)
            parent2 = roulette_wheel_selection(population, fitness_scores)
            child1, child2 = single_point_crossover(parent1, parent2)
            child1 = bit_flip_mutation(child1, mutation_rate)
            child2 = bit_flip_mutation(child2, mutation_rate)
            new_population.extend([child1, child2])
        population = new_population[:pop_size]
    print(f"Final Best Individual: {best_individual}, Fitness: {best_fitness}")

genetic_algorithm(5 , 8, 5, 0.01)
