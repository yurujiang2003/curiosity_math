from sympy import Matrix

# Define the cross product results as matrices
a_cross_b = Matrix([6, -7, 3])
a_cross_c = Matrix([4, 7, 2])
b_cross_c = Matrix([1, -7, 18])

# Compute the terms
term1 = 6 * b_cross_c
term2 = -2 * a_cross_b
term3 = -3 * a_cross_c

# Combine the results
result = term1 + term2 + term3

# Return the final answer
result
