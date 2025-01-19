from sympy import symbols, sqrt, Eq, solve

x = symbols('x', positive=True)
equation = Eq(x - 1/x, 3)

# Calculate (x + 1/x)
y = symbols('y')
identity = Eq((x - 1/x)**2, (x + 1/x)**2 - 4)

# Substitute the known value
lhs_value = 3**2
identity_substituted = identity.subs((x - 1/x)**2, lhs_value)

# Solve for (x + 1/x)^2
y_squared = solve(identity_substituted, (x + 1/x)**2)[0]

# Take the positive square root
final_answer = sqrt(y_squared)

final_answer
