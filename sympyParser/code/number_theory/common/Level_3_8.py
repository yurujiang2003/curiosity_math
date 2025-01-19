from sympy import divisors, prod

x = 12
factors = [d for d in divisors(x) if d > 1 and d < x]
result = prod(factors)
result
