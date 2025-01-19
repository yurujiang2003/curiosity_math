from sympy import symbols, exp, I, Abs

# Define the complex numbers
theta1, theta2, theta3 = symbols('theta1 theta2 theta3')
z1 = exp(I * theta1)
z2 = 2 * exp(I * theta2)
z3 = 3 * exp(I * theta3)

# Calculate |z1 + z2 + z3|
result = Abs(z1 + z2 + z3)

# Evaluate the result
final_answer = result.simplify()
final_answer
