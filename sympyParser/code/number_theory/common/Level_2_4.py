from sympy import symbols, S, isprime

n = symbols('n', integer=True)
p_values = [2, 3, 5, 7, 11, 13, 17]
solution = None

for p in p_values:
    n_value = (13 * p - 1) / (p + 1)
    if n_value.is_integer:
        if isprime((n_value + 1) / (13 - n_value)):
            solution = n_value

solution
