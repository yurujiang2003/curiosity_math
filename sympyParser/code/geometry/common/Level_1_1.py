from sympy import sin, cos, pi

theta = 180 * pi / 180  # Convert degrees to radians
tan_theta = sin(theta) / cos(theta)
result = tan_theta.evalf()
result
