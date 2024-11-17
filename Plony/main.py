# main.py

import configparser
from algorytm import EGA
import Visualization
import torch
from analytical_solution import AnalyticalSolution
import sys

# Read parameters from config.cfg
config = configparser.ConfigParser()
config.read('config.cfg')

a = float(config['Parameters']['a'])
x0 = float(config['Parameters']['x0'])
N_list = [int(n) for n in config['Parameters']['N'].split(',')]
population_size = int(config['Parameters']['population_size'])
num_generations = int(config['Parameters']['num_generations'])
mutation_rate = float(config['Parameters']['mutation_rate'])
elitism_rate = float(config['Parameters']['elitism_rate'])

# Zapisz oryginalny stdout
original_stdout = sys.stdout

# Otwórz plik logu
log_filename = 'simulation_log.txt'
log_file = open(log_filename, 'w')

# Przekieruj stdout do pliku logu i terminala
class Logger(object):
    def __init__(self, terminal, log_file):
        self.terminal = terminal
        self.log_file = log_file

    def write(self, message):
        self.terminal.write(message)
        self.log_file.write(message)

    def flush(self):
        self.terminal.flush()
        self.log_file.flush()

sys.stdout = Logger(sys.stdout, log_file)

# Wykrywanie dostępności GPU
device = 'cuda' if torch.cuda.is_available() else 'cpu'
print(f"Using device: {device}\n")

print("Algorithm Parameters:")
print(f"a = {a}")
print(f"x0 = {x0}")
print(f"N = {N_list}")
print(f"Population Size = {population_size}")
print(f"Number of Generations = {num_generations}")
print(f"Mutation Rate = {mutation_rate}")
print(f"Elitism Rate = {elitism_rate}\n")

for N in N_list:
    print(f"\n========== Uruchamianie algorytmu dla N = {N} ==========\n")
    # Obliczanie rozwiązania analitycznego
    analytical = AnalyticalSolution(a, x0, N)
    analytical_value = analytical.compute_optimal_value()
    analytical_u = analytical.compute_optimal_harvest()

    print(f"Wartość optymalna analityczna dla N = {N}: {analytical_value:.4f}")
    print(f"Optymalne sterowania u_k dla N = {N}:")
    for k, u_k in enumerate(analytical_u, start=1):
        print(f"u_{k} = {u_k:.4f}")

    # Uruchomienie algorytmu EGA
    ega = EGA(a, x0, N, population_size, num_generations, mutation_rate, elitism_rate, device=device)
    ega.run()

    # Pobranie wyników
    best_solution = ega.get_best_solution()
    best_fitness = ega.get_best_fitness()
    fitness_history = ega.get_fitness_history()

    print(f"\nBest solution found by EGA for N = {N}:")
    for k, u_k in enumerate(best_solution):
        print(f"u_{k} = {u_k:.4f}")

    print(f"\nBest fitness (objective function value) for N = {N}: {best_fitness:.4f}")

    # Obliczanie stanów x_k dla najlepszego rozwiązania EGA
    x_ega = [x0]
    for u_k in best_solution:
        x_next = a * x_ega[-1] - u_k
        x_ega.append(x_next)

    # Obliczanie stanów x_k dla rozwiązania analitycznego
    x_analytical = [x0]
    for u_k in analytical_u:
        x_next = a * x_analytical[-1] - u_k
        x_analytical.append(x_next)

    print("\nStates x_k over periods for EGA solution:")
    for k, x_k in enumerate(x_ega):
        print(f"x_{k} = {x_k:.4f}")

    print("\nStates x_k over periods for Analytical solution:")
    for k, x_k in enumerate(x_analytical):
        print(f"x_{k} = {x_k:.4f}")

    # Obliczanie różnicy między wynikami EGA a rozwiązaniem analitycznym
    difference = abs(best_fitness - analytical_value)
    print(f"\nDifference between EGA result and analytical solution for N = {N}: {difference:.4f}")

    # Wizualizacja
    Visualization.plot_convergence(fitness_history, N, analytical_value)
    Visualization.plot_solution(best_solution, analytical_u, x_ega, x_analytical, N)
    Visualization.plot_fitness_over_generations(fitness_history, N, analytical_value)

# Przywróć oryginalny stdout i zamknij plik logu
sys.stdout = original_stdout
log_file.close()
#dodac srednie przystosowanie i wykres jak byly szukane te parametry , na osi x beda iteracje
#jak sie sterowania przedstawiaja
#w sprawozdaniu porównac z wynikami z ksiazki trzeba!
#lepiej zrobic w wykresach slupkowych
