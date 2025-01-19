from sympy import symbols, expand, mod

k1, k2 = symbols('k1 k2')
a = 4 * k1 + 2
b = 4 * k2 + 2

product = expand(a * b)
units_digit = mod(product, 4)

units_digit
