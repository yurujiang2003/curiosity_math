from sympy import binomial

n = 8
r = 6
result = binomial(n, r)
result = binomial(n, n - r)  # Using the property binomial(n, r) = binomial(n, n - r)
final_answer = result
final_answer
