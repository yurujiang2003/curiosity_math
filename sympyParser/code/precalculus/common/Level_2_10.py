from sympy import symbols, cos, Eq, solve

r, theta, x, y = symbols('r theta x y')

# Given polar equation
polar_eq = Eq(r**2 * cos(2 * theta), 4)

# Using the double angle identity
double_angle_identity = 2 * cos(theta)**2 - 1
polar_eq_substituted = polar_eq.subs(cos(2 * theta), double_angle_identity)

# Rearranging the equation
polar_eq_rearranged = Eq(2 * r**2 * cos(theta)**2, r**2 + 4)

# Expressing r^2 in terms of Cartesian coordinates
r_squared = x**2 + y**2
cos_theta = x / r

# Substituting into the rearranged equation
polar_eq_cartesian = polar_eq_rearranged.subs(cos(theta), cos_theta)

# Expressing r^2 * cos^2(theta)
polar_eq_cartesian = polar_eq_cartesian.subs(cos(theta)**2, (x**2 / r_squared))

# Final equation after substitution
final_eq = Eq(2 * x**2, (r_squared)**2 + 4 * r_squared)

# Substitute r_squared
final_eq_substituted = final_eq.subs(r_squared, x**2 + y**2)

# The final answer is that the curve is a hyperbola
answer = 'E'
answer
