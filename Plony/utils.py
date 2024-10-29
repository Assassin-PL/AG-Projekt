# utils.py

import numpy as np

def initialize_population(population_size, N, a, x0):
    population = []
    u0 = (a - 1) * x0  # Wartość równowagi dla u_k
    for _ in range(population_size):
        u = u0 + np.random.uniform(-0.5 * u0, 0.5 * u0, size=N)  # Losowe odchylenia wokół u0
        u = np.clip(u, 0, a * x0)  # Zapewnienie u_k >= 0 i u_k <= a * x0
        population.append(u)
    return np.array(population)
