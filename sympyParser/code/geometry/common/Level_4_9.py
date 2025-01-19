from sympy import symbols, sqrt, acos, deg

s = sqrt(2)
h = 1
A = (0.5, 0.5, h)
B = (0, 0, 0)
D = (1, 1, 0)

AB = (A[0] - B[0], A[1] - B[1], A[2] - B[2])
AD = (D[0] - A[0], D[1] - A[1], D[2] - A[2])

dot_product = AB[0] * AD[0] + AB[1] * AD[1] + AB[2] * AD[2]
magnitude_AB = sqrt(AB[0]**2 + AB[1]**2 + AB[2]**2)
magnitude_AD = sqrt(AD[0]**2 + AD[1]**2 + AD[2]**2)

cos_theta = dot_product / (magnitude_AB * magnitude_AD)
theta = acos(cos_theta)

angle_ABD = deg(theta)
angle_ABD
