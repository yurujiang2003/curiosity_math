from sympy import symbols, floor

m = symbols('m')
count = 0

for m_value in range(1, 1001):
    if m_value == 1:
        continue
    elif m_value == 2:
        count += 1
    else:
        count += 1

count
