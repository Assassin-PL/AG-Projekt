# mutation.py

import numpy as np

def gaussian_mutation(offspring, mutation_rate, a, x0):
    num_offspring, num_genes = offspring.shape
    for i in range(num_offspring):
        if np.random.rand() < mutation_rate:
            gene_indices = np.random.choice(num_genes, size=1)
            for gene_index in gene_indices:
                offspring[i, gene_index] += np.random.normal(0, 0.1)
                # Zapewnienie u_k >= 0
                offspring[i, gene_index] = max(0, offspring[i, gene_index])
    return offspring
