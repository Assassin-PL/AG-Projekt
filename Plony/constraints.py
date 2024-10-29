# constraints.py

import numpy as np

def ensure_constraints(population, a, x0):
    corrected_population = []
    for individual in population:
        u = individual.copy()
        x = np.zeros(len(u) + 1)
        x[0] = x0
        for k in range(len(u)):
            # Zapewnienie u_k >= 0 i u_k <= a * x_k
            max_u = a * x[k]
            u[k] = np.clip(u[k], 0, max_u)
            x[k+1] = a * x[k] - u[k]
            if x[k+1] < 0:
                u[k] = a * x[k]  # Ustawienie u_k na maksymalną wartość
                x[k+1] = 0
        # Korekta ostatniego u_k, aby spełnić x_0 = x_N
        delta = x[-1] - x0
        u[-1] -= delta
        u[-1] = np.clip(u[-1], 0, a * x[-2])
        x[-1] = a * x[-2] - u[-1]
        corrected_population.append(u)
    return np.array(corrected_population)
