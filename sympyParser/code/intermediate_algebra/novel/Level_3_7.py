from sympy import symbols, summation, Rational

n = symbols('n')
a_n = (-1)**(n + 1) * (3 * n + 2)
S = summation(a_n, (n, 1, 100))
S.evalf()
