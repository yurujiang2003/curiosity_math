from sympy import isprime, symbols

composite_sum = 0
for num in range(11, 20):
    if not isprime(num):
        composite_sum += num

composite_sum
