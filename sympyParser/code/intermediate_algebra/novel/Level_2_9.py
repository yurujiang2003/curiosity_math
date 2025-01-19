from sympy import symbols, solve, Abs

k = symbols('k')
m = 32 - 4*k
n = 3*k + 1

m_minus_n = m - n
abs_m_minus_n = Abs(m_minus_n)

min_value = min(abs_m_minus_n.subs(k, i) for i in range(6))
min_value
