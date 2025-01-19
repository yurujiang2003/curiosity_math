from sympy import symbols, sqrt, Eq, solve

x = symbols('x', positive=True)
equation = Eq(x - 1/x, 3)

# Square both sides
squared_eq = Eq((x - 1/x)**2, 9)

# Expand and simplify
expanded_eq = Eq(x**2 - 2 + 1/x**2, 9)
simplified_eq = Eq(x**2 + 1/x**2, 11)

# Use the identity to find x + 1/x
final_eq = Eq((x + 1/x)**2, 13)

# Solve for x + 1/x
result = solve(final_eq, x + 1/x)[0]
result
