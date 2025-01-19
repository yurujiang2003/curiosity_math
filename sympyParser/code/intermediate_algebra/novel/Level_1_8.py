from sympy import Interval

# Define the range of f(x)
f_range = Interval(-3, 5)

# Transform the range for h(x) = 2f(x) - 7
h_range = Interval(2 * f_range.start - 7, 2 * f_range.end - 7)

# Return the final range of h(x)
h_range
