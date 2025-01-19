from sympy import symbols, solve, lcm

a, b = symbols('a b', integer=True)

# Equations based on the problem
eq1 = 3 * max(2, a) - 2 * (2 + a)
eq2 = 3 * max(1, b) - 2 * (1 + b)

# Solve for a and b
solutions = []
for a_val in range(0, 10):  # Testing a from 0 to 9
    for b_val in range(0, 10):  # Testing b from 0 to 9
        if eq1.subs(a, a_val).evalf() == 0 and eq2.subs(b, b_val).evalf() == 0:
            solutions.append((a_val, b_val))

# Calculate the smallest t
min_t = float('inf')
for a_val, b_val in solutions:
    t = 2**a_val * 3**b_val
    if t > 0 and t < min_t:
        min_t = t

min_t
