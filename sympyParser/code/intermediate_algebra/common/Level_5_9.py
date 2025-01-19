from sympy import symbols, mod, floor

x, y, z = symbols('x y z')

count = 0

for x_val in range(20):
    i_x = [1, 1j, -1, -1j][x_val % 4]

    for y_val in range(20):
        angle = (y_val * 3.14159 / 4) % (2 * 3.14159)
        r = 2 ** (y_val / 2)
        one_plus_i_y = r * (cos(angle) + 1j * sin(angle))

        if i_x == one_plus_i_y:
            for z_val in range(20):
                if z_val != i_x:
                    count += 1

        if i_x != one_plus_i_y:
            for z_val in range(20):
                if z_val == i_x or z_val == one_plus_i_y:
                    count += 1

final_count = count
final_count
