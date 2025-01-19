from sympy import symbols, sqrt, Eq, solve

# Define variables
k = symbols('k')

# Radius of the larger circle
r_large = sqrt(8**2 + 6**2)

# Distance QR
QR = 3

# Equation for the radius of the smaller circle
r_small = abs(k)
equation = Eq(r_large - r_small, QR)

# Solve for k
solution = solve(equation, k)

# Return the final answer
solution
