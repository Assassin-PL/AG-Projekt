# Visualization.py

import numpy as np
import matplotlib.pyplot as plt

def plot_convergence(fitness_history, N):
    plt.figure(figsize=(10, 6))
    generations = np.arange(len(fitness_history))
    plt.plot(generations, fitness_history, marker='o', linestyle='-')
    plt.xlabel('Generacja')
    plt.ylabel('Najlepsze przystosowanie')
    plt.title(f'Konwergencja Algorytmu Genetycznego dla N = {N}')
    plt.grid(True)
    # plt.show()
    # Jeśli chcesz zapisać wykres:
    plt.savefig(f'convergence_N_{N}.png')


def plot_solution(u, a, x0, N):
    x = [x0]
    for u_k in u:
        x_next = a * x[-1] - u_k
        x.append(x_next)

    fig, ax1 = plt.subplots(figsize=(10, 6))

    color = 'tab:blue'
    ax1.set_xlabel('Okres k')
    ax1.set_ylabel('Stan x_k', color=color)
    ax1.plot(range(len(x)), x, marker='o', color=color, label='Stan x_k')
    ax1.tick_params(axis='y', labelcolor=color)
    ax1.grid(True)

    ax2 = ax1.twinx()  # Dzielony wykres dla u_k
    color = 'tab:red'
    ax2.set_ylabel('Zbiór u_k', color=color)
    ax2.step(range(len(u)), u, where='post', color=color, label='Zbiór u_k')
    ax2.tick_params(axis='y', labelcolor=color)

    plt.title(f'Optymalny Zbiór i Stan w Czasie dla N = {N}')
    fig.tight_layout()
    # plt.show()
    # Jeśli chcesz zapisać wykres:
    plt.savefig(f'solution_N_{N}.png')


def plot_fitness_over_generations(fitness_values, N):
    """
    Wykres wartości funkcji celu dla każdego pokolenia.

    :param fitness_values: Lista wartości funkcji celu w kolejnych pokoleniach.
    :param N: Aktualna wartość N.
    """
    plt.figure(figsize=(10, 6))
    generations = np.arange(len(fitness_values))
    plt.plot(generations, fitness_values, marker='o', linestyle='-')
    plt.xlabel('Generacja')
    plt.ylabel('Wartość funkcji celu')
    plt.title(f'Wartość Funkcji Celu w Kolejnych Generacjach dla N = {N}')
    plt.grid(True)
    # plt.show()
    # Jeśli chcesz zapisać wykres:
    plt.savefig(f'objective_function_N_{N}.png')
