from sympy import symbols, exp, cos, pi, simplify, re

# Define the complex numbers for the vertices of the heptagon
A = exp(2 * pi * 1j * 0 / 7)
B = exp(2 * pi * 1j * 1 / 7)
D = exp(2 * pi * 1j * 3 / 7)
G = exp(2 * pi * 1j * 6 / 7)

# Calculate the centroid M of triangle ABD
M = (A + B + D) / 3

# Calculate the cosine of the angle GOM
cos_angle_GOM = re(G * M.conjugate()) / (abs(G) * abs(M))

# Calculate cos^2(angle GOM)
cos_squared_angle_GOM = cos_angle_GOM**2

# Simplify the result
final_answer = simplify(cos_squared_angle_GOM)
final_answer
