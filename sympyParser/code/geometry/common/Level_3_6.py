from sympy import symbols, sqrt, N

# Define variables
x, y = symbols('x y')

# Coordinates of downtown St. Paul
S = (0, 0)

# Coordinates of the airport A
A_x = -4 * sqrt(2)
A_y = -4 * sqrt(2)

# Set up equations for downtown Minneapolis M
eq1 = A_x - (x + 5 * sqrt(2))
eq2 = A_y - (y - 5 * sqrt(2))

# Solve for x and y
M_solution = (N(solve(eq1, x)[0]), N(solve(eq2, y)[0]))

# Calculate distance between S and M
distance = sqrt((M_solution[0] - S[0])**2 + (M_solution[1] - S[1])**2)

# Round to the nearest integer
final_distance = round(N(distance))

final_distance
