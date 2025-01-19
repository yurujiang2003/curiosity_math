from sympy import binomial

# Given values
C_15_8 = 6435
C_16_9 = 11440
C_16_10 = 8008

# Calculate C(15, 10)
C_15_10 = binomial(15, 10)

# Calculate C(15, 5) using the identity
C_15_5 = C_16_9 - binomial(15, 4)

# Calculate C(15, 4)
C_15_4 = binomial(15, 4)

# Calculate C(16, 5)
C_16_5 = C_15_5 + C_15_4

# Final answer
final_answer = C_15_10

final_answer
