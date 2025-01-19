from sympy import symbols, Eq, solve

x, y, a = symbols('x y a')

# Substitute x = 3 into the equations
x_value = 3

# First equation: 4x - 3y = 2a
eq1 = Eq(4*x_value - 3*y, 2*a)

# Second equation: 2x + y = 3a
eq2 = Eq(2*x_value + y, 3*a)

# Solve eq2 for y
y_expr = solve(eq2, y)[0]

# Substitute y in eq1
eq1_substituted = eq1.subs(y, y_expr)

# Solve for a
a_value = solve(eq1_substituted, a)[0]

a_value
