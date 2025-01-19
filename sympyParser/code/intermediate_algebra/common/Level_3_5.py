from sympy import symbols, Piecewise, oo, S

x = symbols('x')
f = Piecewise((x**2, x <= 0), (x**3 - 5, x > 0))

range1 = S.Reals.intersect(S.Reals(-5, oo))  # Range for x > 0
range2 = S.Reals.intersect(S.Reals(0, oo))   # Range for x <= 0

final_range = range1.union(range2)
final_range
