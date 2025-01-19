from sympy import I, sqrt, exp, pi

theta = -2 * pi / 3
z = (4 - sqrt(3)) + (-1 - 4 * sqrt(3)) * I
rotation_factor = exp(I * theta)
result = z * rotation_factor
result
