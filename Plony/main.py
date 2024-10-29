# main.py

import configparser
from algorytm import EGA
import Visualization

# Odczyt parametrów z pliku config.cfg
config = configparser.ConfigParser()
config.read('config.cfg')

a = float(config['Parameters']['a'])
x0 = float(config['Parameters']['x0'])
N = int(config['Parameters']['N'])
population_size = int(config['Parameters']['population_size'])
num_generations = int(config['Parameters']['num_generations'])
mutation_rate = float(config['Parameters']['mutation_rate'])
elitism_rate = float(config['Parameters']['elitism_rate'])

# Wyświetlenie parametrów algorytmu
print("Parametry algorytmu:")
print(f"a = {a}")
print(f"x0 = {x0}")
print(f"N = {N}")
print(f"Rozmiar populacji = {population_size}")
print(f"Liczba generacji = {num_generations}")
print(f"Prawdopodobieństwo mutacji = {mutation_rate}")
print(f"Elitarność = {elitism_rate}\n")

# Tworzenie instancji algorytmu EGA
ega = EGA(a, x0, N, population_size, num_generations, mutation_rate, elitism_rate)

# Uruchomienie algorytmu
ega.run()

# Pobranie wyników
best_solution = ega.get_best_solution()
best_fitness = ega.get_best_fitness()
fitness_history = ega.get_fitness_history()

# Wyświetlenie wyników
print("Najlepsze znalezione rozwiązanie:")
for k, u_k in enumerate(best_solution):
    print(f"u_{k} = {u_k:.4f}")
print(f"\nNajlepsze przystosowanie (wartość funkcji celu): {best_fitness:.4f}")

# Obliczenie stanów x_k dla najlepszego rozwiązania
x = [x0]
for u_k in best_solution:
    x_next = a * x[-1] - u_k
    x.append(x_next)

print("\nStany x_k w kolejnych okresach:")
for k, x_k in enumerate(x):
    print(f"x_{k} = {x_k:.4f}")

# Wizualizacja wyników
Visualization.plot_convergence(fitness_history)
Visualization.plot_solution(best_solution, a, x0)
