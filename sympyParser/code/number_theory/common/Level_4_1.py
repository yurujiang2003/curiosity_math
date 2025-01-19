from sympy import primerange, N

def fifth_number_with_three_divisors():
    primes = list(primerange(1, 30))  # Get a list of prime numbers
    squares = [p**2 for p in primes]   # Calculate the squares of the primes
    return squares[4]                  # Return the fifth number

result = fifth_number_with_three_divisors()
result
