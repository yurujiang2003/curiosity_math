from sympy import symbols, Eq, solve, sqrt

# Define variables
a, b, x = symbols('a b x')

# Area equation
area_eq = Eq(a * b, 8)

# Pythagorean theorem equation
pythagorean_eq = Eq(a**2 + b**2, 144)

# Express b in terms of a
b_expr = 8 / a

# Substitute b in the second equation
substituted_eq = area_eq.subs(b, b_expr)

# Substitute into the second equation
second_eq = pythagorean_eq.subs(b, b_expr)

# Solve for a^2
quadratic_eq = Eq(a**4 - 144 * a**2 + 64, 0)
solutions = solve(quadratic_eq, a**2)

# Calculate sin A
sin_A = sqrt(solutions[0]) / 12
sin_squared_A = sin_A**2

# Calculate sin 2A
sin_2A = 2 * sin_A * sqrt(1 - sin_squared_A)

# Return the final answer
sin_2A.evalf()
