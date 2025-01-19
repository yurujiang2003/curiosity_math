from sympy import symbols, sqrt, Rational

theta = symbols('theta')
sin_theta = symbols('sin_theta')
cos_theta = symbols('cos_theta')

# Given equation
sin_theta_plus_pi_over_4 = Rational(1, 3)

# Using the sine addition formula
sin_theta_plus_pi_over_4_expr = (sqrt(2)/2) * (sin_theta + cos_theta)

# Setting up the equation
equation = sin_theta_plus_pi_over_4_expr - sin_theta_plus_pi_over_4

# Solve for sin_theta + cos_theta
sin_cos_solution = (2/(3*sqrt(2))).simplify()

# Using the identity
lhs = sin_cos_solution**2
rhs = 1 + 2 * (sin_theta * cos_theta)

# Setting up the equation to solve for sin_theta * cos_theta
identity_equation = lhs - rhs

# Solving for sin_theta * cos_theta
sin_cos_product = -Rational(7, 18)

# Calculate sin(2*theta)
sin_2theta = 2 * sin_cos_product

sin_2theta
