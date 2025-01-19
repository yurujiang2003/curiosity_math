from sympy import factorint

n = 2400
prime_factors = factorint(n)
total_prime_factors = sum(prime_factors.values())
total_prime_factors
