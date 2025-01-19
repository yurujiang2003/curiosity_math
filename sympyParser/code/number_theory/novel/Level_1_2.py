from sympy import isprime, nextprime

def smallest_reversible_prime(start):
    n = nextprime(start)
    while True:
        reversed_n = int(str(n)[::-1])
        if isprime(reversed_n):
            return n
        n = nextprime(n)

result = smallest_reversible_prime(17)
result
