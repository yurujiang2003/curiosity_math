from sympy import symbols, simplify

# Define variables
a, b, c = 1990, 1000, 990

# Calculate the components
sum_abc = a + b + c
abc = a * b * c

# Calculate squares and products
a2 = a**2
b2 = b**2
c2 = c**2
ab = a * b
ac = a * c
bc = b * c

# Apply the identity
numerator = (sum_abc * (a2 + b2 + c2 - ab - ac - bc)) - 3 * abc
denominator = abc

# Final expression
result = simplify(numerator / denominator)
result
