from sympy import symbols, solve, Integer

n = symbols('n', integer=True)
perfect_square = n**2 - 12
x = (perfect_square / 4).simplify()

least_sum = None
for i in range(4, 100):  # Arbitrarily chosen upper limit for n
    if (i**2 - 12) > 0 and (i**2 - 12) % 4 == 0:
        x_value = (i**2 - 12) // 4
        if x_value > 0 and x_value % 2 == 0:
            current_sum = 4 * x_value + 12
            if least_sum is None or current_sum < least_sum:
                least_sum = current_sum

least_sum
