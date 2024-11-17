# Visualization.py

import numpy as np
import matplotlib.pyplot as plt

def plot_convergence(fitness_history, N, analytical_value):
    plt.figure(figsize=(10, 6))
    generations = np.arange(len(fitness_history))
    avg_fitness = np.mean(fitness_history)
    max_plot_value = 2 * avg_fitness  # 200% średniej wartości

    # Filtracja wartości powyżej 200% średniej
    filtered_fitness = np.minimum(fitness_history, max_plot_value)

    plt.plot(generations, filtered_fitness, marker='o', linestyle='-', label='Najlepsze przystosowanie EGA')
    plt.axhline(y=analytical_value, color='r', linestyle='--', label='Rozwiązanie analityczne')
    plt.xlabel('Generacja')
    plt.ylabel('Najlepsze przystosowanie')
    plt.title(f'Konwergencja Algorytmu Genetycznego dla N = {N}\nŚrednie przystosowanie: {avg_fitness:.4f}')
    plt.legend()
    plt.grid(True)
    plt.ylim([0, max_plot_value * 1.1])  # Dodatkowe 10% dla estetyki wykresu
    plt.savefig(f'convergence_N_{N}.png')
    plt.close()

def plot_fitness_over_generations(fitness_values, N, analytical_value):
    plt.figure(figsize=(10, 6))
    generations = np.arange(len(fitness_values))
    avg_fitness = np.mean(fitness_values)
    max_plot_value = 2 * avg_fitness  # 200% średniej wartości

    # Filtracja wartości powyżej 200% średniej
    filtered_fitness = np.minimum(fitness_values, max_plot_value)

    plt.bar(generations, filtered_fitness, color='skyblue', label='Wartość funkcji celu')
    plt.axhline(y=analytical_value, color='r', linestyle='--', label='Rozwiązanie analityczne')
    plt.xlabel('Generacja')
    plt.ylabel('Wartość funkcji celu')
    plt.title(f'Wartość Funkcji Celu w Kolejnych Generacjach dla N = {N}\nŚrednia wartość: {avg_fitness:.4f}')
    plt.legend()
    plt.grid(True)
    plt.ylim([0, max_plot_value * 1.1])  # Dodatkowe 10% dla estetyki wykresu
    plt.savefig(f'objective_function_N_{N}.png')
    plt.close()

def plot_solution(u_ega, u_analytical, x_ega, x_analytical, N):
    periods = range(len(u_ega))

    # Wykres sterowań u_k
    plt.figure(figsize=(10, 6))
    plt.plot(periods, u_ega, marker='o', linestyle='-', label='u_k EGA')
    plt.plot(periods, u_analytical, marker='x', linestyle='--', label='u_k Analityczne')
    plt.xlabel('Okres k')
    plt.ylabel('Sterowanie u_k')
    plt.title(f'Sterowania u_k dla N = {N}')
    plt.legend()
    plt.grid(True)
    plt.savefig(f'u_k_N_{N}.png')
    plt.close()

    # Wykres stanów x_k
    periods_x = range(len(x_ega))
    plt.figure(figsize=(10, 6))
    plt.plot(periods_x, x_ega, marker='o', linestyle='-', label='x_k EGA')
    plt.plot(periods_x, x_analytical, marker='x', linestyle='--', label='x_k Analityczne')
    plt.xlabel('Okres k')
    plt.ylabel('Stan x_k')
    plt.title(f'Stany x_k dla N = {N}')
    plt.legend()
    plt.grid(True)
    plt.savefig(f'x_k_N_{N}.png')
    plt.close()
