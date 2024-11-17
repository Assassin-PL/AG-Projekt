# utils.py

import torch

def initialize_population(population_size, N, a, x0, device='cpu'):
    # Inicjalizacja sterowań u_k z trendem wzrostowym
    u_init = torch.zeros((population_size, N), device=device)
    for i in range(population_size):
        # Generuj rosnące sterowania
        u0 = (torch.rand(1, device=device) * 0.1 * a * x0).item()  # Mała wartość początkowa (skalar)
        u_end = (torch.rand(1, device=device) * 0.9 * a * x0).item()  # Większa wartość końcowa (skalar)
        u = torch.linspace(u0, u_end, steps=N, device=device)
        u += torch.rand(N, device=device) * 0.05 * a * x0  # Małe zakłócenia
        u = torch.clamp(u, min=0, max=a * x0)
        u_init[i] = u

    # Iteracyjne dostrajanie sterowań, aby spełnić ograniczenie x_0 = x_N
    max_iterations = 10
    tolerance = 1e-3
    for i in range(population_size):
        u = u_init[i]
        for _ in range(max_iterations):
            x = [x0]
            for u_k in u:
                x_next = a * x[-1] - u_k
                x.append(x_next)
            delta = x[-1] - x0
            if abs(delta) < tolerance:
                break
            # Skaluj sterowania proporcjonalnie
            influence = torch.tensor([a ** (N - k - 1) for k in range(N)], device=device)
            total_influence = torch.sum(influence)
            u_adjustment = delta / total_influence
            correction = u_adjustment * influence
            u -= correction
            # Upewnij się, że sterowania są w dopuszczalnym zakresie
            u = torch.clamp(u, min=0, max=a * x0)
        u_init[i] = u

    return u_init