from sympy import symbols, simplify

# Define the variable
x = 3

# Calculate the expression step by step
step1 = x * x
step2 = x + x
step3 = x * step2
step4 = x**3

# Substitute the values back into the expression
result = simplify(step1 + step3 - step4)

# Return the final answer
result
