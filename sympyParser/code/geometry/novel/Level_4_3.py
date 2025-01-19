from sympy import symbols, sqrt, diff, solve

a = symbols('a')
diameter = 100
radius = diameter / 2

# Area function
A = (1/2) * a * sqrt(diameter**2 - a**2)

# Derivative of the area function
A_prime = diff(A, a)

# Solve for critical points
critical_points = solve(A_prime, a)

# Calculate maximum area
max_area = A.subs(a, critical_points[0]).evalf()

max_area
