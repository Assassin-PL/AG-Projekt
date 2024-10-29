# algorytm.py

import numpy as np
from fitness import calculate_fitness
from selection import tournament_selection
from crossover import arithmetic_crossover
from mutation import gaussian_mutation
from constraints import ensure_constraints
from utils import initialize_population

class EGA:
    def __init__(self, a, x0, N, population_size, num_generations, mutation_rate, elitism_rate):
        self.a = a
        self.x0 = x0
        self.N = N
        self.population_size = population_size
        self.num_generations = num_generations
        self.mutation_rate = mutation_rate
        self.elitism_rate = elitism_rate

        # Inicjalizacja populacji
        self.population = initialize_population(population_size, N, a, x0)
        self.fitness_history = []
        self.best_solution = None
        self.best_fitness = None

    def run(self):
        for generation in range(self.num_generations):
            # Obliczanie przystosowania
            fitness_scores = calculate_fitness(self.population, self.a, self.x0)

            # Zapis najlepszego przystosowania
            self.fitness_history.append(np.max(fitness_scores))

            # Wybór elity
            num_elites = int(self.elitism_rate * self.population_size)
            elites_indices = np.argsort(fitness_scores)[-num_elites:]
            elites = self.population[elites_indices]

            # Selekcja rodziców
            parents = tournament_selection(self.population, fitness_scores, self.population_size - num_elites)

            # Generowanie potomstwa
            offspring = []
            for i in range(0, len(parents), 2):
                parent1 = parents[i]
                parent2 = parents[(i + 1) % len(parents)]
                child1, child2 = arithmetic_crossover(parent1, parent2)
                offspring.append(child1)
                offspring.append(child2)
            offspring = np.array(offspring)

            # Mutacja
            offspring = gaussian_mutation(offspring, self.mutation_rate, self.a, self.x0)

            # Zapewnienie ograniczeń
            offspring = ensure_constraints(offspring, self.a, self.x0)

            # Tworzenie nowej populacji
            self.population = np.vstack((elites, offspring[:self.population_size - num_elites]))

            # Opcjonalne wyświetlanie postępu
            if generation % 10 == 0:
                best_fitness = np.max(fitness_scores)
                print(f'Generacja {generation}: Najlepsze przystosowanie = {best_fitness}')

        # Po ewolucji, wybór najlepszego rozwiązania
        fitness_scores = calculate_fitness(self.population, self.a, self.x0)
        best_index = np.argmax(fitness_scores)
        self.best_solution = self.population[best_index]
        self.best_fitness = fitness_scores[best_index]

    def get_best_solution(self):
        return self.best_solution

    def get_best_fitness(self):
        return self.best_fitness

    def get_fitness_history(self):
        return self.fitness_history
