from sympy import sqrt, pi

A = (-4, 5, -17)
B = (34, 15, 5)

d = sqrt((B[0] - A[0])**2 + (B[1] - A[1])**2 + (B[2] - A[2])**2)
r = 13 * sqrt(3)

circumference = 2 * pi * r
circumference
