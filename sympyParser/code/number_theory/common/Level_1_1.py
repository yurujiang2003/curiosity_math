from sympy import primerange, max

primes = list(primerange(1, 40))
largest_primes = sorted(primes)[-2:]
greatest_product = largest_primes[0] * largest_primes[1]
greatest_product
