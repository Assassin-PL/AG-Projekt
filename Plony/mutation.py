# mutation.py

import torch

def gaussian_mutation(offspring, mutation_rate, a, x0, device='cpu'):
    num_offspring, num_genes = offspring.shape
    mutation_mask = (torch.rand((num_offspring, num_genes), device=device) < mutation_rate).float()
    gaussian_noise = torch.randn((num_offspring, num_genes), device=device) * 0.1
    mutation = gaussian_noise * mutation_mask
    offspring += mutation

    # Ensure u_k >= 0 and u_k <= a * x0
    offspring = torch.clamp(offspring, min=0, max=a * x0)
    return offspring

def non_uniform_mutation(offspring, mutation_rate, a, x0, generation, max_generations, b=2, device='cpu'):
    num_offspring, num_genes = offspring.shape
    mutation_mask = (torch.rand((num_offspring, num_genes), device=device) < mutation_rate)

    # Minimalne i maksymalne wartości genów
    v_min = torch.zeros((num_offspring, num_genes), device=device)
    v_max = torch.full((num_offspring, num_genes), a * x0, device=device)

    # Losowe wartości r i kierunek mutacji
    r = torch.rand((num_offspring, num_genes), device=device)
    direction = torch.rand((num_offspring, num_genes),
                           device=device) < 0.5  # True dla dodatniej zmiany, False dla ujemnej

    # Obliczanie Delta
    tau = generation / max_generations
    exponent = (1 - tau) ** b
    delta = (v_max - offspring) * (1 - r ** exponent) * direction.float() + \
            (offspring - v_min) * (1 - r ** exponent) * (~direction).float()

    # Zastosowanie mutacji
    offspring = offspring + mutation_mask.float() * delta

    # Zapewnienie ograniczeń u_k >= 0 i u_k <= a * x0
    offspring = torch.clamp(offspring, min=0, max=a * x0)
    return offspring

