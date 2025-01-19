from sympy import Matrix

# Define the vectors
a = Matrix([6, -7, 3])
b = Matrix([1, -7, 18])
c = Matrix([4, 7, 2])

# Calculate (2b) x (3c)
term1 = 6 * b

# Calculate (2b) x a
term2 = -2 * a

# Calculate -a x (3c)
term3 = -3 * c

# Combine the results
result = term1 + term2 + term3
result
