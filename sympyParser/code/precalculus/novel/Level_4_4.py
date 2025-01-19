from sympy import symbols, sin, solve, sqrt, Matrix, acos, deg

# Define variables
theta, k = symbols('theta k')

# Norms of the vectors
norm_a = 1/sqrt(2)
norm_b = 1/sqrt(3)
norm_c = 1/sqrt(6)

# Step 1: From the norm of a
cross_product_norm = (norm_b * norm_c * sin(theta)).subs(sin(theta), (1/3/sqrt(2)) * k)
eq1 = abs(k) * (1/(3*sqrt(2))) * sin(theta) - norm_a

# Solve for k in terms of theta
k_solution = solve(eq1, k)[0]

# Step 2: Norm of a + b + c
norm_a_sq = norm_a**2
norm_b_sq = norm_b**2
norm_c_sq = norm_c**2
lhs = norm_a_sq + norm_b_sq + norm_c_sq

# Calculate the left-hand side
lhs_value = lhs + 2 * (k_solution * (1/(3*sqrt(2))) * (1/3*sqrt(2)) * (1/3*sqrt(2)) * cos(theta))

# Set the equation to 1
eq2 = lhs_value - 1

# Solve for theta
theta_solution = solve(eq2, theta)

# Convert to degrees
angle_degrees = deg(theta_solution[0])

angle_degrees
print(angle_degrees)