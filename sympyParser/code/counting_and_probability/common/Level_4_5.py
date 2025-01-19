from sympy import symbols, Matrix

# Define the number of steps
n_steps = 15

# Initialize state variables
a, b, c = [0] * (n_steps + 1), [0] * (n_steps + 1), [0] * (n_steps + 1)

# Initial conditions
a[0], b[0], c[0] = 1, 0, 0

# Compute the values iteratively
for n in range(n_steps):
    a[n + 1] = b[n]
    b[n + 1] = a[n] + b[n] + c[n]
    c[n + 1] = b[n]

# Final answer: number of ways to be at vertex 0 after 15 steps
final_answer = a[n_steps]
final_answer
