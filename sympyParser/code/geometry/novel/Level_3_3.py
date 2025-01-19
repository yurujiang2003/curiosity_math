from sympy import pi

r1 = 2
r2 = 4
r3 = 6
r4 = 8

A1 = pi * r1**2
A2 = pi * r2**2
A3 = pi * r3**2
A4 = pi * r4**2

shaded_area_1 = A2 - A1
shaded_area_2 = A3 - A2
shaded_area_3 = A4 - A3

total_shaded_area = shaded_area_1 + shaded_area_2 + shaded_area_3

total_shaded_area
