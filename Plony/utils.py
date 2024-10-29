# utils.py

import torch

def initialize_population(population_size, N, a, x0, device='cpu'):
    u0 = (a - 1) * x0  # Wartość równowagi dla u_k
    u_init = u0 + torch.randn((population_size, N), device=device) * (0.1 * u0)
    u_init = torch.clamp(u_init, min=0, max=a * x0)
    return u_init
