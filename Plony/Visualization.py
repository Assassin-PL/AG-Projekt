# Visualization.py

import numpy as np
import matplotlib.pyplot as plt


def plot_convergence(fitness_history):
    plt.figure(figsize=(10, 6))
    plt.plot(fitness_history)
    plt.xlabel('Generacja')
    plt.ylabel('Najlepsze przystosowanie')
    plt.title('Konwergencja Algorytmu Genetycznego')
    plt.grid(True)
    plt.show()


def plot_solution(u, a, x0):
    N = len(u)
    x = np.zeros(N + 1)
    x[0] = x0
    for k in range(N):
        x[k + 1] = a * x[k] - u[k]

    fig, ax1 = plt.subplots(figsize=(10, 6))

    color = 'tab:blue'
    ax1.set_xlabel('Okres k')
    ax1.set_ylabel('Stan x_k', color=color)
    ax1.plot(range(N + 1), x, marker='o', color=color, label='Stan x_k')
    ax1.tick_params(axis='y', labelcolor=color)
    ax1.grid(True)

    ax2 = ax1.twinx()  # Dzielony wykres dla u_k
    color = 'tab:red'
    ax2.set_ylabel('Zbiór u_k', color=color)
    ax2.step(range(N), u, where='post', color=color, label='Zbiór u_k')
    ax2.tick_params(axis='y', labelcolor=color)

    plt.title('Optymalny Zbiór i Stan w Czasie')
    fig.tight_layout()
    plt.show()
