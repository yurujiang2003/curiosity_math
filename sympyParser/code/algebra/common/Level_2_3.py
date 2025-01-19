from sympy import symbols, Rational, simplify

# Define the operations
star = '*'
star_value = 10 * 7
star_value = 70

star2 = '*'
star2_value = 24 * 9
star2_value = 216

# Calculate the fraction
result = Rational(star_value, star2_value)

# Simplify the fraction
final_answer = simplify(result)
final_answer
