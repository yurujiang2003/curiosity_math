from sympy import symbols, mod

# Define the smallest three-digit positive integer
n = 100

# Check the remainder when n is divided by 7
remainder = mod(n, 7)

# Calculate the difference needed to reach 1 (mod 7)
difference = (1 - remainder) % 7

# Find the smallest three-digit integer that is congruent to 1 (mod 7)
result = n + difference

result
