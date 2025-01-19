from sympy import binomial

# Given values
C_15_8 = 6435
C_16_9 = 11440
C_16_10 = 8008

# Calculate C(15, 9)
C_15_9 = C_16_9 - C_15_8

# Calculate C(15, 10)
C_15_10 = C_16_10 - C_15_9

C_15_10
