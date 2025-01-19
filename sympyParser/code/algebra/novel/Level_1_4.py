from sympy import Rational

# Define the fractions
num1 = Rational(3, 8)
num2 = Rational(7, 8)
denom = Rational(4, 5)

# Simplify the numerator
numerator = num1 + num2
simplified_numerator = numerator.simplify()

# Substitute back into the original expression and simplify
result = simplified_numerator / denom
final_answer = result.simplify()

final_answer
