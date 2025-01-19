from sympy import symbols, floor

m = symbols('m')
count = 0

for m_value in range(1, 1001):
    if m_value == 1 or m_value > 1:
        count += 1

count
