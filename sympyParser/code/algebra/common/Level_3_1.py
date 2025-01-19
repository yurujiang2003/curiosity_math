from sympy import log, Rational

# Define the base and the argument
base = 5**Rational(1, 3)
argument = 5**3

# Use the change of base formula
result = log(argument, base)

# Evaluate the result
final_answer = result.evalf()
final_answer
