from sympy import Mod

# Define the numbers
a = 121
b = 122
c = 123

# Calculate each number modulo 4
mod_a = Mod(a, 4)
mod_b = Mod(b, 4)
mod_c = Mod(c, 4)

# Combine the results
result = Mod(mod_a * mod_b * mod_c, 4)

# Return the final answer
result
