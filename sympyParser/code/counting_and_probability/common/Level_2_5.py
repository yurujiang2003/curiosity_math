from sympy import factorial, lcm

# Calculate 6! and (4!)^2
factorial_6 = factorial(6)
factorial_4_squared = factorial(4)**2

# Calculate the least common multiple
result = lcm(factorial_6, factorial_4_squared)

result
