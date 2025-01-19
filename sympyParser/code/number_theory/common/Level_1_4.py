from sympy import symbols, ceiling

k = symbols('k')
N = 13 * ceiling(10 / 13)
M = 13 * (99 // 13)

result = M + N
result
