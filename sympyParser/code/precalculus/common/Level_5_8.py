from sympy import I, exp, pi, sqrt

z1 = -5 + 3*I
z2 = 8 - I

theta1 = pi / 3
theta2 = -pi / 3

z2_minus_z1 = z2 - z1

e_theta1 = exp(I * theta1)
e_theta2 = exp(I * theta2)

c1 = z1 + (z2_minus_z1 * e_theta1)
c2 = z1 + (z2_minus_z1 * e_theta2)

product_c1_c2 = c1 * c2
product_c1_c2
