from sympy import symbols, floor, sqrt, simplify

x = symbols('x')

f_x = (-1)**floor(x) * sqrt(1/4 - (x - floor(x) - 1/2)**2)
f_neg_x = (-1)**floor(-x) * sqrt(1/4 - (-x - floor(-x) - 1/2)**2)

# Determine the relationship between f(-x) and f(x)
is_odd = simplify(f_neg_x + f_x) == 0

if is_odd:
    result = "odd"
else:
    result = "neither"

result
