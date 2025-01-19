from sympy import symbols, simplify, Rational

s = symbols('s')
expression = 4*s**2 + 28*s + 45

# Step 2: Factor out the coefficient of s^2
factored_expression = 4 * (s**2 + 7*s) + 45

# Step 3: Complete the square
half_coefficient = Rational(7, 2)
squared_term = half_coefficient**2

# Step 4: Rewrite the expression
completed_square_expression = 4 * ((s + half_coefficient)**2 - squared_term) + 45

# Step 5: Distribute and combine constants
final_expression = simplify(completed_square_expression)

# Identify q
q_value = final_expression.as_coefficients_dict()[1]  # Extracting the constant term
q_value = q_value - 49 + 45  # Combine constants

q_value
