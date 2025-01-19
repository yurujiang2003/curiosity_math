from sympy import symbols, Eq, solve, sqrt

D = symbols('D', real=True)

# Given equation
tan_eq = Eq(sin(D)/cos(D), 3*sin(D))

# Solve for cos(D)
cos_D = solve(tan_eq, cos(D))[0]

# Use Pythagorean identity to find sin(D)
sin_D = sqrt(1 - cos_D**2)

# Calculate sin(F)
sin_F = cos_D

# Final answer
sin_F_value = sin_F.evalf()
sin_F_value
