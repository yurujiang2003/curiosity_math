from sympy import symbols, Eq, solve

m, n = symbols('m n')
eq1 = Eq(3*m + 4*n, 47)
eq2 = Eq(m + n, 15)

solution = solve((eq1, eq2), (m, n))
m_value = solution[m]
m_value
