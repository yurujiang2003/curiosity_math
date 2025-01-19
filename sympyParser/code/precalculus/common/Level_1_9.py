from sympy import symbols, tan, solve, pi

n = symbols('n')
k = symbols('k', integer=True)

# Equation for the tangent function
equation = tan(n * pi / 180) - tan(252 * pi / 180)

# General solution for n
general_solution = 252 + k * 180

# Solve for k such that -90 < n < 90
valid_n = []
for k_value in range(-2, 2):  # Check k from -2 to 1
    n_value = general_solution.subs(k, k_value)
    if -90 < n_value < 90:
        valid_n.append(n_value)

# Return the valid integer solution
final_answer = int(valid_n[0]) if valid_n else None
final_answer
