from sympy import symbols

x, y, z = symbols('x y z')

count = 0

for x_val in range(20):
    i_x = [1, 1j, -1, -1j][x_val % 4]
    for y_val in range(20):
        if y_val % 2 == 0:
            one_plus_i_y = 2**(y_val / 2)
        else:
            one_plus_i_y = 2**(y_val / 2) * (1 / (2**(y_val / 2))) * 1j

        for z_val in range(20):
            if len({i_x, one_plus_i_y, z_val}) == 2:
                count += 1

result = count
result
