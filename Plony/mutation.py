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
