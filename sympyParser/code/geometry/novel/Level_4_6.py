from sympy import sqrt

# Define the sides of the triangle
AB = 10
AC = 17
BC = 21

# Calculate the semi-perimeter
s = (AB + AC + BC) / 2

# Calculate the area using Heron's formula
A = sqrt(s * (s - AB) * (s - AC) * (s - BC))

# Calculate the inradius
r = A / s

# Return the final answer rounded to the nearest tenth
r.evalf()
