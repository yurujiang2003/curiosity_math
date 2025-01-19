from sympy import symbols, Eq, solve

# Define the variables
x, y = symbols('x y')

# Known lengths
AB = 1
BC = 2
CD = 3
DE = 4
EF = 2
FG = 2

# Equations based on the problem
eq1 = Eq(AB + CD + EF, x + y)  # 1 + 3 + 2 = x + y
eq2 = Eq(BC + DE + FG, AB + CD + y + x)  # 2 + 4 + 2 = 1 + 3 + y + x

# Solve for x and y
solution = solve((eq1, eq2), (x, y))
x_value = solution[x]
y_value = solution[y]

# Calculate the perimeter
P = AB + BC + CD + DE + EF + FG + x_value + y_value
P
