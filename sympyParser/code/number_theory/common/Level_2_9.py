from sympy import Mod

# Define the numbers
a = 121
b = 122
c = 123

# Calculate the modulo 4 residues
residue_a = Mod(a, 4)
residue_b = Mod(b, 4)
residue_c = Mod(c, 4)

# Calculate the product modulo 4
result = Mod(residue_a * residue_b * residue_c, 4)

# Return the final answer
result
