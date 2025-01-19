from sympy import symbols, Eq, sin, cos, solve

b, a, c, x, y, z, theta = symbols('b a c x y z theta')

# Given relationships
x = (3 * b) / 2  # AD = (3/2) * AC
eq1 = Eq(b**2 + a**2, c**2)  # Pythagorean theorem

# Using the sine rule in triangles ACD and ABD
sin_2theta = 2 * sin(theta) * cos(theta)
eq2 = Eq(b / x, sin_2theta / (sin(theta) * (b / x)))  # From the sine rule

# Solve for y/z
# BC = BD + CD => a = z + y
# y/z = 2/1 => y = 2z
eq3 = Eq(y, 2 * z)

# Substitute y in terms of z into the equation
eq4 = eq3.subs(y, 2 * z)

# Solve for z in terms of a
z_solution = solve(eq4, z)[0]

# Calculate CD/BD
ratio = (2 * z_solution) / z_solution
final_answer = ratio.simplify()

final_answer
