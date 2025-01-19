from sympy import symbols, sqrt, simplify

# Define variables
r = symbols('r')
a = -1
b = 5
c = 1

# Calculate the new radius r
r_value = sqrt(5) - 1

# Express r in the form (a + sqrt(b)) / c
r_expression = simplify((a + sqrt(b)) / c)

# Calculate a + b + c
result = a + b + c

result
