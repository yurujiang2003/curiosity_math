from sympy import symbols, binomial, Rational

n = 7
k = 4
p = Rational(1, 5)
q = 1 - p

binom_coeff = binomial(n, k)
probability = binom_coeff * (p**k) * (q**(n-k))

final_answer = probability.simplify()
final_answer
