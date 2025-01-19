from sympy import symbols, simplify

n = symbols('n')
odd_numbers_sum = (2*n - 1) + (2*n + 1) + (2*n + 3) + (2*n + 5)
simplified_sum = simplify(odd_numbers_sum)

greatest_factor = simplified_sum / 8
greatest_factor
