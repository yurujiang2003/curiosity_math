from sympy import symbols, simplify

K, L = symbols('K L')
operation = (K + L) * (K - L)

result = simplify(operation.subs({K: 6, L: 5}))
result
