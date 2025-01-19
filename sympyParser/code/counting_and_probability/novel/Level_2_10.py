from sympy import binomial, isprime

n = 6
row = [binomial(n, k) for k in range(n + 1)]
prime_count = sum(1 for number in row if isprime(number))

prime_count
