from sympy import symbols, Eq, solve

E = 14
b = symbols('b')
V = b + 1
F = b + 1

# Euler's formula
equation = Eq(V - E + F, 2)

# Solve for b
solution = solve(equation, b)[0]

# Total number of vertices
total_vertices = solution + 1
total_vertices
