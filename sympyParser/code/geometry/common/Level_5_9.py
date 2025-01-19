from sympy import symbols, pi, sqrt

# Define variables
r, h = symbols('r h')

# Volume of the cylinder
V_cylinder = 60

# Express h in terms of r
h_expr = V_cylinder / (pi * r**2)

# Radius of the circumscribing sphere
R = sqrt(r**2 + (h_expr / 2)**2)

# Volume of the sphere
V_sphere = (4/3) * pi * R**3

# Calculate the volume of the sphere for the specific case
V_sphere_value = V_sphere.subs(h, h_expr).subs(r, sqrt(60/(pi*h_expr))).simplify()

# Final answer
final_volume = V_sphere_value.subs(h, h_expr).evalf()
final_volume
