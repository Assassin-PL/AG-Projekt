# analytical_solution.py

class AnalyticalSolution:
    def __init__(self, a, x0, N):
        self.a = a
        self.x0 = x0
        self.N = N

    def compute_optimal_value(self):
        """
        Computes the analytical optimal value J* based on the formula:
        J* = x0 * (a - 1)^2
        """
        optimal_value = ((self.x0 * (self.a ** self.N - 1) ** 2) / ( (self.a  - 1)*(self.a ** (self.N - 1) ) )) ** 0.5
        return optimal_value

    def compute_optimal_harvest(self):
        """
        Computes the optimal harvest u_k analytically.
        For this specific problem, the optimal harvest in each period is constant:
        u_k = [x0 * (a^N - 1)] / [N * a^{N - k}]
        """
        optimal_u_sequence = []
        for k in range(1, self.N + 1):
            numerator = self.x0 * (self.a ** self.N - 1)
            denominator = self.N * (self.a ** (self.N - k))
            u_k = numerator / denominator
            optimal_u_sequence.append(u_k)
        return optimal_u_sequence
