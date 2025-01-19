from sympy import binomial, Rational

n = 7
k = 4
p = Rational(1, 5)
q = 1 - p

binom_coeff = binomial(n, k)
p_k = p**k
q_n_k = q**(n - k)

probability = binom_coeff * p_k * q_n_k
probability
