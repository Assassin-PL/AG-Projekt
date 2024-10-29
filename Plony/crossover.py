# crossover.py

import torch

def arithmetic_crossover(parents1, parents2):
    alpha = torch.rand((parents1.shape[0], 1), device=parents1.device)
    child1 = alpha * parents1 + (1 - alpha) * parents2
    child2 = alpha * parents2 + (1 - alpha) * parents1
    offspring = torch.cat([child1, child2], dim=0)
    return offspring
