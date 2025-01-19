from sympy import sqrt, Rational

# Define the trigonometric values
cos_45 = sqrt(2) / 2
cos_30 = sqrt(3) / 2
sin_45 = sqrt(2) / 2
sin_30 = Rational(1, 2)

# Compute cos(15 degrees) using the cosine difference identity
cos_15 = cos_45 * cos_30 + sin_45 * sin_30

# Simplify the expression
cos_15_simplified = cos_15.simplify()

# Return the final answer
cos_15_simplified
