from sympy import symbols, Piecewise, sqrt, plot

x = symbols('x')

# Define the original function f(x)
f = Piecewise(
    (-2 - x, (x >= -3) & (x <= 0)),
    (sqrt(4 - (x - 2)**2) - 2, (x > 0) & (x <= 2)),
    (2 * (x - 2), (x > 2) & (x <= 3))
)

# Define the transformed function -f(-x)
transformed_f = -f.subs(x, -x)

# Plot the original and transformed functions
p1 = plot(f, (x, -3, 3), show=False, line_color='red', title='y = f(x)')
p2 = plot(transformed_f, (x, -3, 3), show=False, line_color='blue', title='y = -f(-x)')

# Combine plots
p1.extend(p2)
p1.show()

# Return the answer for the graph of y = -f(-x)
answer = 'D'
answer
