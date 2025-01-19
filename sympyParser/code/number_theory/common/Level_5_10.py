from sympy import divisor_sigma, factorint

A = divisor_sigma(500)
prime_factors = factorint(A)
distinct_primes = list(prime_factors.keys())
result = sum(distinct_primes)
result
