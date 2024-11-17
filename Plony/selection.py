# selection.py

import torch

def tournament_selection(population, fitness_scores, num_parents, tournament_size=5, device='cpu'):
    population_size = population.shape[0]
    parents = []

    for _ in range(num_parents):
        indices = torch.randint(0, population_size, (tournament_size,), device=device)
        selected_fitness = fitness_scores[indices]
        winner_index = indices[torch.argmax(selected_fitness)]
        parents.append(population[winner_index])

    return torch.stack(parents)


def deterministic_tournament_selection(population, fitness_scores, num_parents, tournament_size=5, device='cpu'):
    population_size = population.shape[0]
    parents = []

    # Tworzenie indeksów osobników
    indices = torch.arange(population_size)

    # Losowe permutowanie indeksów
    shuffled_indices = indices[torch.randperm(population_size)]

    # Podział populacji na grupy turniejowe
    num_tournaments = population_size // tournament_size
    for i in range(num_tournaments):
        tournament_indices = shuffled_indices[i * tournament_size: (i + 1) * tournament_size]
        tournament_fitness = fitness_scores[tournament_indices]
        winner_index = tournament_indices[torch.argmax(tournament_fitness)]
        parents.append(population[winner_index])

    # Jeśli potrzebujemy więcej rodziców niż turniejów, losowo wybieramy z wygranych
    while len(parents) < num_parents:
        extra_parent = population[torch.randint(0, population_size, (1,), device=device).item()]
        parents.append(extra_parent)

    return torch.stack(parents)

def mate_parents(parents):
    num_parents = parents.shape[0]
    if num_parents % 2 != 0:
        parents = parents[:-1]  # Usuń ostatniego rodzica, aby mieć parzystą liczbę
    half = num_parents // 2
    parents1 = parents[:half]
    parents2 = parents[half:2*half]
    return parents1, parents2

