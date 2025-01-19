from sympy import symbols, Eq, solve

# Define variables
b1 = 16  # length of the longer base
b2 = 4   # length of the shorter base
AD = 10  # length of the non-parallel sides
x, h = symbols('x h')

# Calculate x
eq1 = Eq(2*x + b2, b1)
x_value = solve(eq1, x)[0]

# Calculate h using Pythagorean theorem
eq2 = Eq(AD**2, x_value**2 + h**2)
h_value = solve(eq2, h)[0]

# Calculate area
area = (1/2) * (b1 + b2) * h_value
area_value = area.evalf()

area_value
