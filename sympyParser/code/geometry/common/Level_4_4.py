from sympy import symbols, pi, simplify

r, h = symbols('r h')
V0 = pi * r**2 * h
r_new = 0.8 * r
h_new = 1.25 * h
V_new = pi * (r_new)**2 * (h_new)

percent_change = (V_new - V0) / V0 * 100
absolute_percent_change = abs(simplify(percent_change))

absolute_percent_change
