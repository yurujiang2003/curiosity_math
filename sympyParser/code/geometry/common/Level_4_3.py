from sympy import symbols, sqrt

# Define the diameter and calculate the radius
diameter = 100
radius = diameter / 2

# Define the length of the legs of the triangle
x = radius * sqrt(2)

# Calculate the area of the triangle
area = (1/2) * x * x

# Return the final answer
area.evalf()
