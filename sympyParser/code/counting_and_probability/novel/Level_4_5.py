from sympy import symbols, Matrix

# Define the number of steps
n_steps = 15

# Initialize a and b
a = [0] * (n_steps + 1)
b = [0] * (n_steps + 1)

# Initial conditions
a[0] = 1
b[0] = 0

# Recurrence relations
for n in range(n_steps):
    a[n + 1] = 2 * b[n]
    b[n + 1] = a[n] + 2 * b[n]

# Total paths
total_paths = 2 ** n_steps

# Probability that the ant is at A_0 after 15 steps
probability = a[n_steps] / total_paths

probability
