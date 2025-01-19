from sympy import log, sqrt, Rational

# Define the base and the argument
base = sqrt(5)**(1/3)
argument = 125

# Rewrite the logarithm using properties
log_value = log(argument, base)

# Calculate the logarithm
log_value = log_value.simplify()

# Final answer
final_answer = log_value.evalf()
final_answer
