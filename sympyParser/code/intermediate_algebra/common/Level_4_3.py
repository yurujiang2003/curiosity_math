from sympy import symbols, expand

x = symbols('x')

# Define the polynomial based on the roots
f_x = 2 * (x**4 - 8*x**3 + 8*x**2 + 52*x - 77)

# Calculate f(1)
result = f_x.subs(x, 1)
result
