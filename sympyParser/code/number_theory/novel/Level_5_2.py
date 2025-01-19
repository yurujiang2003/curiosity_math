from sympy import symbols, prime, factorint

n_values = []
for p1 in range(1, 100):  # Check primes up to 100
    p1 = prime(p1)
    if p1**6 >= 12005:
        break
    for p2 in range(1, 100):
        p2 = prime(p2)
        if p2 >= p1:  # Ensure p2 is different from p1
            continue
        if p1**6 * p2**2 < 12005:
            n = p1**6 * p2**2 - 2005
            if n > 0 and n < 10000:
                n_values.append(n)

result = sum(n_values)
result
