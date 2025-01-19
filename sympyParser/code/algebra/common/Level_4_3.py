from sympy import symbols, solve, sqrt

x = symbols('x')
inequality = (x - 4)**2 - 9

# Solve the equation (x - 4)^2 = 9
critical_points = solve(inequality, x)

# Determine the length of the segment
length = critical_points[1] - critical_points[0]
length
