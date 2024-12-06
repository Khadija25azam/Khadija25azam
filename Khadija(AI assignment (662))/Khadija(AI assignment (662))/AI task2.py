import random

def initialize_population(pop_size, chromosome_length):
    return ["".join(random.choice("01") for _ in range(chromosome_length)) for _ in range(pop_size)]

def fitness_function(individual):
    return individual.count('1') * 2  

def calculate_total_fitness(fitness_scores):
    return sum(fitness_scores)

def calculate_fitness_ratios(fitness_scores):
    total_fitness = calculate_total_fitness(fitness_scores)
    return [f / total_fitness for f in fitness_scores]

def generate_random_pick():
    return random.random()

def roulette_wheel_selection(population, fitness_scores):
    fitness_ratios = calculate_fitness_ratios(fitness_scores)
    cumulative_fitness = [sum(fitness_ratios[:i + 1]) for i in range(len(fitness_ratios))]
    
    pick = generate_random_pick()
    for idx, cum_fit in enumerate(cumulative_fitness):
        if pick <= cum_fit:
            return population[idx], idx  

def visualize_selection(population, fitness_scores):
    print(f"{'Individual':<10} {'Fitness (kg)':<15} {'Fitness Ratio':<15} {'Cumulative Fitness':<20} {'Selected?':<10}")
    
    total_fitness = calculate_total_fitness(fitness_scores)
    fitness_ratios = calculate_fitness_ratios(fitness_scores)
    cumulative_fitness = [sum(fitness_ratios[:i + 1]) for i in range(len(fitness_ratios))]
    
    selected_individual, selected_idx = roulette_wheel_selection(population, fitness_scores)
    
    for idx, (ind, fitness, ratio, cum_fit) in enumerate(zip(population, fitness_scores, fitness_ratios, cumulative_fitness)):
        selected = "Yes" if idx == selected_idx else "No"
        print(f"{ind:<10} {fitness:<15} {ratio:<15.3f} {cum_fit:<20.3f} {selected:<10}")

def genetic_algorithm(pop_size, chromosome_length, generations):
    population = initialize_population(pop_size, chromosome_length)
    
    for gen in range(generations):
        print(f"\nGeneration {gen + 1}")
        
        fitness_scores = [fitness_function(ind) for ind in population]
        
        visualize_selection(population, fitness_scores)
        
        new_population = []
        while len(new_population) < pop_size:
            parent1, _ = roulette_wheel_selection(population, fitness_scores)
            parent2, _ = roulette_wheel_selection(population, fitness_scores)
            new_population.append(parent1)
            new_population.append(parent2)
        
        population = new_population[:pop_size]

pop_size = 5  
chromosome_length = 4  
generations = 5 
genetic_algorithm(pop_size, chromosome_length, generations)
