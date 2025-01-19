from sympy import symbols, Rational

# Define variables
a = 32  # side BC
tan_B = Rational(3, 2)
tan_C = Rational(1, 2)

# Calculate the area using the formula
K = (a**2 * tan_B * tan_C) / (tan_B + tan_C)

# Return the final answer
K.evalf()
