from sympy import symbols, Poly, roots, Rational

x = symbols('x')
f = x**5 + 7*x**4 - 2
r = roots(Poly(f), x)

S = Rational(0)
for a in r.keys():
    term = a**5 / ((a - r.keys()).prod())
    S += term

S = S.simplify()
result = S.evalf()
result
