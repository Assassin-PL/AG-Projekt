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
        penalty += 1e6 * torch.relu(-u_k)
        # Kary za ujemne x_{k+1}
        penalty += 1e6 * torch.relu(-x[:, k+1])

    # Kara za niespełnienie x_0 = x_N
    penalty += 1e6 * torch.abs(x[:, -1] - x0)

    fitness = torch.sum(torch.sqrt(torch.clamp(population, min=0)), dim=1) - penalty

    return fitness
