# fitness.py

import torch

def calculate_fitness(population, a, x0, device='cpu'):
    N = population.shape[1]
    population_size = population.shape[0]

    x = torch.zeros((population_size, N + 1), device=device)
    x[:, 0] = x0

    penalty = torch.zeros(population_size, device=device)

    for k in range(N):
        u_k = population[:, k]
        x[:, k+1] = a * x[:, k] - u_k

    # Kary za ujemne u_k
    penalty += torch.sum(torch.relu(-population) ** 2, dim=1)

    # Kary za ujemne x_k
    penalty += torch.sum(torch.relu(-x[:, 1:]) ** 2, dim=1)

    # Kara za niespełnienie x_0 = x_N
    penalty += (x[:, -1] - x0) ** 2

    # Obliczanie funkcji celu
    objective = torch.sum(torch.sqrt(torch.clamp(population, min=0) + 1e-8), dim=1)

    # Funkcja przystosowania
    fitness = objective - penalty

    # Zapewnienie nieujemnych wartości funkcji przystosowania
    fitness = torch.clamp(fitness, min=0)

    return fitness
