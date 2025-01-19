from sympy import binomial, Rational

n = 3
k = 2
p = Rational(1, 7)
q = 1 - p

probability = binomial(n, k) * (p**k) * (q**(n - k))
probability
