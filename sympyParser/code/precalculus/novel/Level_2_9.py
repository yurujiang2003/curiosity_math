from sympy import symbols, Eq, solve

x, y, z = symbols('x y z')

# Original equation
equation = Eq(x**2 + 2*x + y**2 + 6*y + z**2 - 12*z + 30, 0)

# Completing the square for x
x_square = (x + 1)**2 - 1

# Completing the square for y
y_square = (y + 3)**2 - 9

# Completing the square for z
z_square = (z - 6)**2 - 36

# Substitute back into the equation
new_equation = Eq(x_square + y_square + z_square + 30 - 1 - 9 - 36, 0)

# Simplifying the equation
final_equation = new_equation.simplify()

# Rearranging to standard form
standard_form = final_equation.lhs - 16

# The radius is the square root of 16
radius = 4

radius
