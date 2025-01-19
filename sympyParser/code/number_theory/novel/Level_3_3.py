from sympy import primerange

primes = list(primerange(1, 542))  # 542 is just above the 100th prime
product_units_digit = 0

if 2 in primes and 5 in primes:
    product_units_digit = 0

product_units_digit
