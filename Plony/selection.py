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
