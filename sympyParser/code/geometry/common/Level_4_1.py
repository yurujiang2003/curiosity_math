from sympy import sin, pi, sqrt

angle = 1755
reduced_angle = angle % 360
final_angle = reduced_angle

if final_angle == 315:
    result = -sin(45 * pi / 180)
else:
    result = sin(final_angle * pi / 180)

result
