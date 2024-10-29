# constraints.py

import torch

def ensure_constraints(population, a, x0, device='cpu'):
    N = population.shape[1]
    population_size = population.shape[0]

    x = torch.zeros((population_size, N + 1), device=device)
    x[:, 0] = x0

    u = population.clone()

    for k in range(N):
        max_u = a * x[:, k]
        min_u = torch.zeros_like(max_u)

        u_k = torch.clamp(u[:, k], min=min_u, max=max_u)
        u[:, k] = u_k
        x[:, k+1] = a * x[:, k] - u_k

        # Zapewnienie x_{k+1} >= 0
        negative_x = x[:, k+1] < 0
        if negative_x.any():
            idx = negative_x.nonzero(as_tuple=True)[0]
            u[idx, k] = max_u[idx]
            x[idx, k+1] = 0

    # Korekta ostatniego u_k, aby spełnić x_0 = x_N
    delta = x[:, -1] - x0
    u[:, -1] -= delta

    max_u_last = a * x[:, -2]
    min_u_last = torch.zeros_like(max_u_last)
    u[:, -1] = torch.clamp(u[:, -1], min=min_u_last, max=max_u_last)
    x[:, -1] = a * x[:, -2] - u[:, -1]

    return u
