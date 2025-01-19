from sympy import primerange, sqrt

lower_bound = sqrt(100)
upper_bound = sqrt(300)

primes = list(primerange(int(lower_bound) + 1, int(upper_bound) + 1))
count_of_primes = len(primes)

count_of_primes
