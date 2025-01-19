from sympy import primerange

primes = list(primerange(1, 100))
primes_with_3 = [p for p in primes if p % 10 == 3]
result = len(primes_with_3)
result
