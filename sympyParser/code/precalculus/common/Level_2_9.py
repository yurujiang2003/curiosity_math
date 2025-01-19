from sympy import symbols, sqrt, Eq, simplify

x, y, z = symbols('x y z')

equation = x**2 + 2*x + y**2 + 6*y + z**2 - 12*z + 30

# Completing the square
x_square = (x + 1)**2 - 1
y_square = (y + 3)**2 - 9
z_square = (z - 6)**2 - 36

# Substitute back into the equation
new_equation = Eq(x_square + y_square + z_square + 30 - 1 - 9 - 36, 0)

# Simplifying the equation
simplified_equation = simplify(new_equation)

# Rearranging to find the radius
radius_squared = 16
radius = sqrt(radius_squared)

radius
