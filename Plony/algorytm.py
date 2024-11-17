# algorytm.py

import torch
from fitness import calculate_fitness
from selection import tournament_selection, deterministic_tournament_selection, mate_parents
from crossover import arithmetic_crossover, advanced_blx_alpha_crossover
from mutation import non_uniform_mutation, gaussian_mutation
from constraints import ensure_constraints
from utils import initialize_population

class EGA:
    def __init__(self, a, x0, N, population_size, num_generations, mutation_rate, elitism_rate, device='cpu'):
        self.a = a
        self.x0 = x0
        self.N = N
        self.population_size = population_size
        self.num_generations = num_generations
        self.mutation_rate = mutation_rate
        self.elitism_rate = elitism_rate
        self.device = device

        # Inicjalizacja populacji jako tensor PyTorch na określonym urządzeniu
        self.population = initialize_population(population_size, N, a, x0, device=self.device)
        self.fitness_history = []
        self.best_solution = None
        self.best_fitness = None

    def run(self):
        for generation in range(self.num_generations):
            # Obliczanie przystosowania
            fitness_scores = calculate_fitness(self.population, self.a, self.x0, device=self.device)

            # Zapis najlepszego przystosowania
            best_fitness = torch.max(fitness_scores).item()
            self.fitness_history.append(best_fitness)

            # Wybór elity
            num_elites = int(self.elitism_rate * self.population_size)
            elites_indices = torch.topk(fitness_scores, num_elites).indices
            elites = self.population[elites_indices]

            # Selekcja rodziców
            num_offspring = self.population_size - num_elites
            # parents = tournament_selection(self.population, fitness_scores, num_offspring, device=self.device)
            parents = deterministic_tournament_selection(self.population, fitness_scores, num_offspring, device=self.device)
            # Zapewnienie parzystej liczby rodziców
            if parents.shape[0] % 2 != 0:
                parents = torch.cat([parents, parents[:1]], dim=0)

            # Podział rodziców na pary
            parents1 = parents[::2]
            parents2 = parents[1::2]

            # Krzyżowanie
            offspring = arithmetic_crossover(parents1, parents2, alpha=0.5)
            # offspring = advanced_blx_alpha_crossover(parents1, parents2, generation, self.num_generations, alpha_min=0.1, alpha_max=0.5, a=self.a, x0=self.x0)
            # Nowa funkcja mutacji

            # offspring = gaussian_mutation(offspring, self.mutation_rate, self.a, self.x0, device=self.device)
            offspring = non_uniform_mutation(offspring, self.mutation_rate, self.a, self.x0, generation, self.num_generations, b=2, device=self.device)
            # Zapewnienie ograniczeń
            offspring = ensure_constraints(offspring, self.a, self.x0, device=self.device)

            # Tworzenie nowej populacji
            self.population = torch.cat([elites, offspring], dim=0)[:self.population_size]

            # Opcjonalne wyświetlanie postępu
            if generation % 10 == 0:
                print(f'Generacja {generation}: Najlepsze przystosowanie = {best_fitness}')

        # Po ewolucji, wybór najlepszego rozwiązania
        fitness_scores = calculate_fitness(self.population, self.a, self.x0, device=self.device)
        best_index = torch.argmax(fitness_scores)
        self.best_solution = self.population[best_index].cpu().numpy()
        self.best_fitness = fitness_scores[best_index].item()

    # **Dodanie brakujących metod**
    def get_best_solution(self):
        return self.best_solution

    def get_best_fitness(self):
        return self.best_fitness

    def get_fitness_history(self):
        return self.fitness_history
