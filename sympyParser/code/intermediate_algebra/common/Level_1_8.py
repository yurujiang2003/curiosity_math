from sympy import symbols, Interval

# Define the variable
x = symbols('x')

# Define the range of f(x)
range_f = Interval(-3, 5)

# Transform the range for h(x) = 2f(x) - 7
lower_bound_h = 2 * range_f.start - 7
upper_bound_h = 2 * range_f.end - 7

# Define the range of h(x)
range_h = Interval(lower_bound_h, upper_bound_h)

# Return the final answer
range_h
