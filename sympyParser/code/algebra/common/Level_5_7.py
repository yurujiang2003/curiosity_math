from sympy import symbols, sqrt, solve

k = symbols('k')
x = symbols('x')
y = 3

k_value = 15 * sqrt(24)
y_expr = k_value / sqrt(x)

sqrt_x = solve(y_expr - y, sqrt(x))[0]
x_value = sqrt_x**2

x_value
