from sympy import symbols, Eq, solve

# Define the variables
x, y = symbols('x y')

# Given lengths
AB = 1
BC = 2
CD = 3
DE = 4
EF = 2
FG = 2

# Set up the equations based on the properties of the equiangular octagon
eq1 = Eq(AB + CD + x, BC + DE + y)
eq2 = Eq(EF + y, FG + x)

# Solve the equations
solution = solve((eq1, eq2), (x, y))

# Calculate the perimeter
perimeter = AB + BC + CD + DE + EF + FG + solution[x] + solution[y]
perimeter
