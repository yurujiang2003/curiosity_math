from sympy import symbols, Min

x = symbols('x')
f_values = {1: 2, 3: 0, 5: -2, 6: 0}

min_f_value = Min(*f_values.values())
max_f_inverse = [k for k, v in f_values.items() if v == min_f_value][0]

max_f_inverse
