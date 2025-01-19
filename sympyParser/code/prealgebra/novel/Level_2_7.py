from sympy import symbols, ceiling

n = symbols('n')
multiple_of_5 = 5 * n
value = -32

# Find the smallest integer n such that 5n > -32
n_value = ceiling(value / 5)
smallest_multiple = multiple_of_5.subs(n, n_value)

smallest_multiple
