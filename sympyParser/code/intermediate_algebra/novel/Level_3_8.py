from sympy import symbols, floor, sqrt, Piecewise, simplify

x = symbols('x')

# Define the function f(x)
f_x = (-1)**floor(x) * sqrt(1/4 - (x - floor(x) - 1/2)**2)

# Define f(-x)
f_neg_x = (-1)**floor(-x) * sqrt(1/4 - (-x - floor(-x) - 1/2)**2)

# Simplify the expressions
f_x_simplified = simplify(f_x)
f_neg_x_simplified = simplify(f_neg_x)

# Check if f(-x) == f(x) or f(-x) == -f(x)
is_even = simplify(f_neg_x_simplified == f_x_simplified)
is_odd = simplify(f_neg_x_simplified == -f_x_simplified)

# Determine the result
if is_even:
    result = "even"
elif is_odd:
    result = "odd"
else:
    result = "neither"

result
