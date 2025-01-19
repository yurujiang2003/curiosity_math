from sympy import gcd, mod

m_values = range(1, 9)
n = sum(1 for m in m_values if gcd(m, 8) == 1)
result = mod(3**n, 8)
result
