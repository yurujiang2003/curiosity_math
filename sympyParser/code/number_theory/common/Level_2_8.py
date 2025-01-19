from sympy import symbols, solve, sqrt

n = symbols('n')
sum_expr = 4 * (n**2 - 12) / 4 + 12
k = 2

while True:
    x = k**2 - 3
    if x > 0:
        sum_of_integers = x + (x + 2) + (x + 4) + (x + 6)
        if sqrt(sum_of_integers).is_integer:
            break
    k += 1

sum_of_integers
