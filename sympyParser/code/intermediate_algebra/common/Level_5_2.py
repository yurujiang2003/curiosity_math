from sympy import symbols, Eq, solve

a, b, c = symbols('a b c')

# Define the equations based on the roots
equations = [
    Eq(c**2 + a*c + b, 0),  # Original quadratic equation
    Eq((c**2 - 2)**2 + a*(c**2 - 2) + b, 0)  # Condition for c^2 - 2 being a root
]

# Define the cases to check
cases = [0, 1, -1, 2**0.5, -2**0.5]
valid_quadratics = set()

for case in cases:
    c_val = case
    # Solve for a and b based on the roots
    d_val = -a - c_val
    eq1 = equations[0].subs(c, c_val)
    eq2 = equations[1].subs(c, c_val)

    # Solve the equations
    solutions = solve((eq1, eq2), (a, b))

    for sol in solutions:
        valid_quadratics.add((sol[a], sol[b]))

# Count distinct quadratic equations
final_answer = len(valid_quadratics)
final_answer
