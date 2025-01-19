from sympy import divisor_sigma, primefactors

A = divisor_sigma(500)
distinct_primes = primefactors(A)
result = sum(distinct_primes)
result
