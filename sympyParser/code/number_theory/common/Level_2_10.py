from sympy import *

# Define the modulo
mod = 17

# Calculate each term modulo 17
term1 = 289 % mod
term2 = (9 * (51 % mod)) % mod
term3 = (3**6) % mod
term4 = (4 * (187 % mod)) % mod

# Combine the results
result = (term1 + term2 + term3 + term4) % mod

# Return the final answer
result
