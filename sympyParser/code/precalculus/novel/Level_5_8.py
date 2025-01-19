from sympy import I, sqrt, exp, pi

A = -5 + 3*I
B = 8 - I

# Calculate the vector from A to B
AB = B - A

# Calculate c1
c1 = A + AB * exp(I * pi / 3)

# Calculate c2
c2 = A + AB * exp(-I * pi / 3)

# Calculate the product c1 * c2
product = c1 * c2

product
