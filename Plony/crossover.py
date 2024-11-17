# crossover.py

import torch

def arithmetic_crossover(parents1, parents2, alpha=0.5):
    # Zakładamy, że parents1 i parents2 mają ten sam rozmiar
    num_offspring, num_genes = parents1.shape

    # Obliczanie minimalnych i maksymalnych wartości genów rodziców
    min_genes = torch.min(parents1, parents2)
    max_genes = torch.max(parents1, parents2)

    # Generowanie losowych wartości w rozszerzonym zakresie
    diff = max_genes - min_genes
    lower_bound = min_genes - alpha * diff
    upper_bound = max_genes + alpha * diff

    # Losowanie wartości dla potomków w rozszerzonym zakresie
    offspring = torch.empty((num_offspring, num_genes), device=parents1.device)
    offspring.uniform_(0.0, 1.0)
    offspring = lower_bound + (upper_bound - lower_bound) * offspring

    return offspring


def advanced_blx_alpha_crossover(parents1, parents2, generation, max_generations, alpha_min=0.1, alpha_max=0.5, a=2.0,
                                 x0=110.0):
    num_offspring, num_genes = parents1.shape
    offspring = torch.empty_like(parents1)

    # Obliczanie dynamicznej wartości alpha
    alpha = alpha_max - (generation / max_generations) * (alpha_max - alpha_min)

    # Obliczanie odchylenia standardowego genów w populacji
    population = torch.cat((parents1, parents2), dim=0)
    gene_std = torch.std(population, dim=0)
    max_std = torch.max(gene_std)

    # Unikanie dzielenia przez zero
    if max_std == 0:
        max_std = 1e-8

    # Skalowanie alpha dla każdego genu
    alpha_scaled = alpha * (gene_std / max_std)

    # Krzyżowanie BLX-Alpha dla każdego potomka
    for i in range(num_offspring):
        cmin = torch.min(parents1[i], parents2[i])
        cmax = torch.max(parents1[i], parents2[i])
        I = cmax - cmin

        lower_bound = cmin - alpha_scaled * I
        upper_bound = cmax + alpha_scaled * I

        # Generowanie potomka
        offspring[i] = lower_bound + (upper_bound - lower_bound) * torch.rand(num_genes, device=parents1.device)

    # Zapewnienie ograniczeń u_k >= 0 i u_k <= a * x0
    offspring = torch.clamp(offspring, min=0.0, max=a * x0)

    return offspring
