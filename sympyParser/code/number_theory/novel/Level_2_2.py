from sympy import gcd, symbols

m_values = range(1, 9)
n = sum(1 for m in m_values if gcd(m, 8) == 1)

result = 3**n % 8
result
