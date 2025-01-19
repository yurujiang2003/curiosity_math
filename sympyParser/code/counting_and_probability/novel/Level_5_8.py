from sympy import gcd, Rational

total_outcomes = 6 * 6
relatively_prime_count = 0

for a in range(1, 7):
    for b in range(1, 7):
        if gcd(a, b) == 1:
            relatively_prime_count += 1

probability = Rational(relatively_prime_count, total_outcomes)
probability
