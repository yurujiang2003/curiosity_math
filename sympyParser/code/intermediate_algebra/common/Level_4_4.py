from sympy import symbols, solve

r = symbols('r')
sum_of_roots = 12
product_of_roots = 64

# Since r1 = r2 = r3 = r
r_value = sum_of_roots / 3

# Calculate a using Vieta's second formula
a = 3 * (r_value * r_value)

# Final answer
a_value = a.evalf()
a_value
