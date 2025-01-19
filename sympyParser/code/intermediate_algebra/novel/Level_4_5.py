from sympy import symbols, sqrt, simplify

tau = (1 + sqrt(5)) / 2
S = 1 / tau / (1 - 1/tau)
S = simplify(S)

n = 1 if S == tau else None
n
