from sympy import symbols, expand

m, n = symbols('m n')
a = 4*m + 2
b = 4*n + 2

product = expand(a * b)
units_digit = product % 4

units_digit
