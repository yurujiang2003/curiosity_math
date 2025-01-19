from sympy import symbols, Eq, solve, Matrix

a, b, c = symbols('a b c')

# Define the equations
eq1 = Eq(a + 3*b + 4*c, 25)
eq2 = Eq(a**2 + b**2 + c**2, 25)

# Solve for c in terms of a and b
c_expr = (25 - a - 3*b) / 4

# Substitute c in the second equation
eq2_substituted = eq2.subs(c, c_expr)

# Expand and simplify the equation
eq2_expanded = eq2_substituted.lhs.expand() - eq2_substituted.rhs

# Collect terms
eq2_collected = eq2_expanded.collect(a)

# Coefficients for the quadratic in terms of a
coeffs = eq2_collected.as_coefficients_dict()
A = coeffs.get(a**2, 0)
B = coeffs.get(a, 0)
C = coeffs.get(1, 0)

# Calculate the vertex of the quadratic
a_max = -B / (2 * A)

# Solve for b and c when a is maximized
b_val = 0  # Assume b = 0 for maximization
c_val = (25 - a_max - 3*b_val) / 4

# Check if the solution satisfies the second equation
if a_max**2 + b_val**2 + c_val**2 == 25:
    result = a_max
else:
    result = None

result
