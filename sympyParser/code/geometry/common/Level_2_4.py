from sympy import symbols, sqrt

b1 = 4  # top base
b2 = 16  # bottom base
leg = 10  # length of the legs

# Calculate the height using the Pythagorean theorem
h = sqrt(leg**2 - ((b2 - b1) / 2)**2)

# Calculate the area of the trapezoid
area = (1/2) * (b1 + b2) * h

area.evalf()
