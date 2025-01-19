from sympy import isprime

def smallest_non_prime():
    N = 1
    while True:
        P_N = 7 + 30 * N
        if not isprime(P_N):
            return N
        N += 1

result = smallest_non_prime()
result
