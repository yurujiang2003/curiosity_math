from sympy import gcd

count = 0
for i in range(11, 30):
    if gcd(i, 28) == 1:
        count += 1

count
