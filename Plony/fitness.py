# fitness.py

import numpy as np

def calculate_fitness(population, a, x0):
    fitness_scores = []
    for individual in population:
        u = individual
        x = np.zeros(len(u) + 1)
        x[0] = x0
        penalty = 0
        for k in range(len(u)):
            x[k+1] = a * x[k] - u[k]
            if u[k] < 0:
                penalty += 1e6 * abs(u[k])  # Kara za ujemne u_k
            if x[k+1] < 0:
                penalty += 1e6 * abs(x[k+1])  # Kara za ujemne x_{k+1}
        penalty += 1e6 * abs(x[0] - x[-1])  # Kara za niespełnienie x_0 = x_N
        fitness = np.sum(np.sqrt(np.maximum(u, 0))) - penalty
        fitness_scores.append(fitness)
    return np.array(fitness_scores)
