from sympy import symbols, sqrt, Eq, solve

x, k, y = symbols('x k y')

# Given values
y_value_at_24 = 15
x_value_at_24 = 24

# Finding k
k_value = y_value_at_24 * sqrt(x_value_at_24)

# Setting up the equation for y
y_eq = Eq(y, k_value / sqrt(x))

# Finding x when y = 3
y_value = 3
equation = y_eq.subs(y, y_value)

# Solving for x
x_solution = solve(equation, x)[0]
x_solution
