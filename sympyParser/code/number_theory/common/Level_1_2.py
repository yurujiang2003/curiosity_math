from sympy import isprime, primerange

def smallest_reversible_prime(start):
    for prime in primerange(start + 1, 200):  # Arbitrarily chosen upper limit
        reversed_prime = int(str(prime)[::-1])
        if isprime(reversed_prime):
            return prime

result = smallest_reversible_prime(17)
result
