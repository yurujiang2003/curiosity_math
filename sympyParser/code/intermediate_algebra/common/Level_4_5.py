from sympy import symbols, sqrt, Rational

tau = (1 + sqrt(5)) / 2
S = 1 / (tau - 1)
S_simplified = S.simplify()
n = 1 if S_simplified == tau else None

n
