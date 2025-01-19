from sympy import divisors, Rational

n = 2010
pos_divisors = divisors(n)
num_divisors = len(pos_divisors)

# Each positive divisor has a corresponding negative divisor
total_polynomials = 2 * num_divisors

total_polynomials
