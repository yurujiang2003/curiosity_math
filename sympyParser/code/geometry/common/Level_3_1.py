from sympy import sqrt, Rational

a = 8
b = 15
c = sqrt(a**2 + b**2)

m = Rational(1, 2) * sqrt(2 * a**2 + 2 * b**2 - c**2)
m
