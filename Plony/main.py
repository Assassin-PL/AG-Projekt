# main.py

import configparser
from algorytm import EGA
import Visualization
import torch

# Odczyt parametrów z pliku config.cfg
config = configparser.ConfigParser()
config.read('config.cfg')

a = float(config['Parameters']['a'])
x0 = float(config['Parameters']['x0'])
N_list = [int(n) for n in config['Parameters']['N'].split(',')]
population_size = int(config['Parameters']['population_size'])
num_generations = int(config['Parameters']['num_generations'])
mutation_rate = float(config['Parameters']['mutation_rate'])
elitism_rate = float(config['Parameters']['elitism_rate'])

# Wykrywanie dostępności GPU
device = 'cuda' if torch.cuda.is_available() else 'cpu'
print(f'Używane urządzenie: {device}\n')

# Wyświetlenie parametrów algorytmu
print("Parametry algorytmu:")
print(f"a = {a}")
print(f"x0 = {x0}")
print(f"N = {N_list}")
print(f"Rozmiar populacji = {population_size}")
print(f"Liczba generacji = {num_generations}")
print(f"Prawdopodobieństwo mutacji = {mutation_rate}")
print(f"Elitarność = {elitism_rate}\n")

# Iteracja po liście wartości N
for N in N_list:
    print(f"\n========== Uruchamianie algorytmu dla N = {N} ==========\n")
    # Tworzenie instancji algorytmu EGA
    ega = EGA(a, x0, N, population_size, num_generations, mutation_rate, elitism_rate, device=device)

    # Uruchomienie algorytmu
    ega.run()

    # Pobranie wyników
    best_solution = ega.get_best_solution()
    best_fitness = ega.get_best_fitness()
    fitness_history = ega.get_fitness_history()  # Zawiera najlepsze przystosowanie w każdej generacji

    # Wyświetlenie wyników
    print(f"Najlepsze znalezione rozwiązanie dla N = {N}:")
    for k, u_k in enumerate(best_solution):
        print(f"u_{k} = {u_k:.4f}")
    print(f"\nNajlepsze przystosowanie (wartość funkcji celu) dla N = {N}: {best_fitness:.4f}")

    # Obliczenie stanów x_k dla najlepszego rozwiązania
    x = [x0]
    for u_k in best_solution:
        x_next = a * x[-1] - u_k
        x.append(x_next)

    print("\nStany x_k w kolejnych okresach:")
    for k, x_k in enumerate(x):
        print(f"x_{k} = {x_k:.4f}")

    # Wizualizacja wyników
    Visualization.plot_convergence(fitness_history, N)
    Visualization.plot_solution(best_solution, a, x0, N)
    # Wywołanie nowej funkcji wizualizacyjnej
    Visualization.plot_fitness_over_generations(fitness_history, N)
