from sympy import divisors

n = 24
divs = divisors(n)
count = sum(1 for d in divs if d > 1)
count
