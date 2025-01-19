from sympy import symbols, Eq, solve, sqrt

x = symbols('x')  # AD
y = symbols('y')  # CD
z = symbols('z')  # BD

# Given values
AC = 3
AB = 6
cos_60 = 1/2

# Equations from the Law of Cosines
eq1 = Eq(y**2, AC**2 + x**2 - 2 * AC * x * cos_60)
eq2 = Eq(z**2, AB**2 + x**2 - 2 * AB * x * cos_60)

# Solve for y^2 and z^2
y_squared = solve(eq1, y**2)[0]
z_squared = solve(eq2, z**2)[0]

# BC^2 = (y + z)^2 = y^2 + z^2 + 2yz
BC_squared = (y + z)**2

# Calculate y^2 + z^2
y_z_squared_sum = y_squared + z_squared

# Calculate 2yz
yz = sqrt(y_squared * z_squared)

# Final equation for BC^2
BC_squared_eq = Eq(BC_squared, y_z_squared_sum + 2 * yz)

# Solve for AD (x)
AD_solution = solve(BC_squared_eq, x)
AD_solution
