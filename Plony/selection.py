# selection.py

import numpy as np

def tournament_selection(population, fitness_scores, num_parents, tournament_size=5):
    selected = []
    population_size = len(population)
    for _ in range(num_parents):
        participants_indices = np.random.choice(population_size, tournament_size)
        participants_fitness = fitness_scores[participants_indices]
        winner_index = participants_indices[np.argmax(participants_fitness)]
        selected.append(population[winner_index])
    return np.array(selected)
