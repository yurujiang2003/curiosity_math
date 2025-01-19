from sympy import symbols, Eq, solve, sqrt

x = symbols('x')
y = x**2 - 10*x

# Define the equation in terms of y
equation = Eq(1/(y - 29) + 1/(y - 45) - 2/(y - 69), 0)

# Find a common denominator and simplify
numerator = (y - 45)*(y - 69) + (y - 29)*(y - 69) - 2*(y - 29)*(y - 45)
numerator_simplified = numerator.expand()

# Set the numerator equal to zero and solve for y
y_solution = solve(Eq(numerator_simplified, 0), y)[0]

# Solve for x using the quadratic formula
a = 1
b = -10
c = -y_solution

discriminant = b**2 - 4*a*c
x1 = (10 + sqrt(discriminant)) / (2*a)
x2 = (10 - sqrt(discriminant)) / (2*a)

# Return the positive solution
positive_solution = max(x1, x2)
positive_solution
