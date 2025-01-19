from sympy import symbols, Piecewise, oo, S

x = symbols('x')
f = Piecewise((x**2, x <= 0), (x**3 - 5, x > 0))

range_x_le_0 = S.Reals.intersect(S.Reals[0:oo])  # [0, ∞)
range_x_gt_0 = S.Reals.intersect(S.Reals[-5:oo])  # (-5, ∞)

final_range = range_x_le_0.union(range_x_gt_0)
final_range
