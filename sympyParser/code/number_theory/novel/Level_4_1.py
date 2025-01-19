from sympy import prime

def fifth_number_with_three_divisors():
    primes = [prime(i) for i in range(1, 6)]
    squares = [p**2 for p in primes]
    return squares[4]

result = fifth_number_with_three_divisors()
result
