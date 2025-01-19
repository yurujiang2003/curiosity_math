from sympy import symbols, Eq, solve, sqrt

a, d = symbols('a d')

# First equation: 2a + 4000d = 50
eq1 = Eq(2*a + 4000*d, 50)

# Second equation: a(a + 4000d) = 400
eq2 = Eq(a * (a + 4000*d), 400)

# Solve for d in terms of a using eq1
d_expr = solve(eq1, d)[0]

# Substitute d in eq2
eq2_substituted = eq2.subs(d, d_expr)

# Solve the quadratic equation
a_solutions = solve(eq2_substituted, a)

# Calculate |a1 - a4001| for both solutions
results = []
for a_value in a_solutions:
    d_value = d_expr.subs(a, a_value)
    a4001 = a_value + 4000*d_value
    results.append(abs(a_value - a4001))

final_answer = results
final_answer
