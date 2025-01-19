from sympy import symbols, sqrt, Eq, solve

s = symbols('s')
r = symbols('r')

# Setting up the equation
equation = Eq((r - 3*s)**2 + (r - s)**2, (r + s)**2)

# Solving the equation
solutions = solve(equation, r)

# Filtering the solution for r > s
final_solution = [sol for sol in solutions if sol > s]

# Calculating r/s
result = final_solution[0] / s
result
