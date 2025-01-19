from sympy import factorint

number = 2400
factors = factorint(number)
total_primes = sum(factors.values())
total_primes
