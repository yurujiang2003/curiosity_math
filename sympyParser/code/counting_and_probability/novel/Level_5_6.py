from sympy import pi, Rational

R = 1  # Radius of the circle (can be any positive value)
arc_length = Rational(2, 3) * (2 * pi)  # Favorable arc length
total_length = 2 * pi  # Total circle length

P = (arc_length / total_length)**2
P
