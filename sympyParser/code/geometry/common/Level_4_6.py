from sympy import sqrt

AB = 10
AC = 17
BC = 21

s = (AB + AC + BC) / 2
A = sqrt(s * (s - AB) * (s - AC) * (s - BC))
r = A / s

r.evalf()
