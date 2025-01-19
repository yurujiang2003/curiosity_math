from sympy import sqrt, symbols, solve, Rational

# Define the lengths
AB = sqrt(30)
AC = sqrt(6)
BC = sqrt(15)

# Semi-perimeter
s = (AB + AC + BC) / 2

# Area of triangle ABC using Heron's formula
K_ABC = sqrt(s * (s - AB) * (s - AC) * (s - BC))

# Coordinates
b = BC
x, y = symbols('x y')

# Equations based on distance formulas
eq1 = x**2 + y**2 - 30
eq2 = (x - b)**2 + y**2 - 6

# Solve for x and y
sol = solve((eq1, eq2), (x, y))
A = sol[0]  # Take the first solution

# Area of triangle ABC
area_ABC = K_ABC

# Area of triangle ADB
# Since angle ADB is right, we can use the coordinates
AD = sqrt(A[0]**2 + A[1]**2)  # Distance from A to D (which is the same as A to B)
area_ADB = Rational(1, 2) * AB * A[1]

# Ratio of areas
ratio = area_ADB / area_ABC
ratio.evalf()
