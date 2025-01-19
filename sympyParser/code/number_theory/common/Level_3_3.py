from sympy import primerange

# Get the first 100 prime numbers
primes = list(primerange(1, 542))  # 542 is just above the 100th prime (541)

# Calculate the units digit of the product
units_digit = 0 if 2 in primes and 5 in primes else None

units_digit
