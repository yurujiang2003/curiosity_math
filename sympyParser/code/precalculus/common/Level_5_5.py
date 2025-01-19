from sympy import symbols, Eq, solve, Rational

r = symbols('r')
k1 = 1
k2 = Rational(1, 2)
k3 = Rational(1, 3)
k4 = -1/r

lhs = (k1 + k2 + k3 + k4)**2
rhs = 2 * (k1**2 + k2**2 + k3**2 + k4**2)

equation = Eq(lhs, rhs)
solution = solve(equation, r)

solution
