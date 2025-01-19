from sympy import isprime

def least_prime_greater_than_25():
    k = 1
    while True:
        p = 25 * k + 2
        if p > 25 and isprime(p):
            return p
        k += 1

result = least_prime_greater_than_25()
result
