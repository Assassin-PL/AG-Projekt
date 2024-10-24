# Elitist Genetic Algorithm (EGA) for Harvest Collection Problem

This project implements an Elitist Genetic Algorithm (EGA) to solve the harvest collection problem, which is a constrained optimization task. The goal is to maximize the harvest yield while respecting the growth equation and constraints.

## Problem Description

The harvest collection problem involves maximizing the final yield over a given number of time periods (`N`), subject to the following constraints:

- **Growth equation:**  
  \( x_{n+1} = a \cdot x_n - u_n \), where:
  - \( a \) is a constant growth factor (e.g., 1.1)
  - \( x_0 \) is the initial state (e.g., 100)
  - \( u_n \) is the control variable representing the amount harvested in period \( n \)

- **Control constraints:**  
  \( u_n \geq 0 \) for all \( n \), ensuring non-negative harvests.

- **Equality constraint:**  
  \( \sum_{n=0}^{N-1} u_n = x_0 \), meaning that the total amount harvested over all periods equals the initial state.

## Elitist Genetic Algorithm (EGA)

The EGA is an evolutionary algorithm that aims to find the optimal harvesting strategy by iteratively evolving a population of solutions. It uses the concept of elitism, where the best-performing individuals (solutions) from each generation are carried over to the next generation to preserve high-quality solutions.

### Key Features of EGA:

1. **Elitism:** The best individuals are directly copied to the next generation, ensuring that the quality of solutions is maintained.
2. **Genetic Operators:**
   - **Selection:** Tournament selection is used to choose parents for crossover.
   - **Crossover:** One-point crossover is applied to combine solutions from two parents.
   - **Mutation:** Random perturbations are applied to introduce variability in the offspring.
3. **Constraint Handling:** Special mechanisms are implemented to ensure that the sum of harvested amounts satisfies the equality constraint, and all values remain non-negative.

## Parameters

The algorithm allows for the following customizable parameters:
- `N`: Number of periods (e.g., [2, 4, 10, 20, 45])
- `a`: Growth factor (default: 1.1)
- `x0`: Initial state (default: 100)
- `Population size`: Number of solutions in the population
- `Number of generations`: Total number of iterations for evolution
- `Mutation rate`: Probability of mutation applied to an individual
- `Elitism rate`: Fraction of top individuals retained in the next generation

## Installation and Usage

### Prerequisites

Ensure you have Python 3.x and the necessary libraries installed:
- `numpy` for numerical operations
- `matplotlib` (optional, for plotting results)

### Running the Algorithm

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/harvest-ega.git
   cd harvest-ega
