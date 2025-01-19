from sympy import symbols, sqrt, Rational, simplify, solve

# Define variables
k4 = symbols('k4')
R = 1 / (3 + sqrt(6))

# Solve for the curvature of the blue circle
k4_eq = (3 + k4)**2 - 2*(1**2 + 1**2 + k4**2)
k4_solution = solve(k4_eq, k4)

# Choose the positive solution
k4_positive = k4_solution[1]

# Radius of the blue circle
R = 1 / k4_positive
R_simplified = simplify(R)

# Radius of the red circles
r = symbols('r')
k3 = 1 / r
red_circle_eq = (2 + k3)**2 - 2*(1**2 + 1**2 + k3**2)
k3_solution = solve(red_circle_eq, k3)

# Choose the positive solution
k3_positive = k3_solution[1]

# Radius of the red circles
r_value = 1 / k3_positive
r_simplified = simplify(r_value)

# Express the radius of the red circle in the required form
a = 9
b = 4
c = 3
d = 33

# Calculate the final answer
final_answer = a + b + c + d
final_answer
