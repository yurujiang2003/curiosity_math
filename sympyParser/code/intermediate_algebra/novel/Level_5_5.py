from sympy import factorint, divisors

n = 2010
prime_factors = factorint(n)

num_divisors = 1
for exponent in prime_factors.values():
    num_divisors *= (exponent + 1)

total_polynomials = 2 * num_divisors
total_polynomials
