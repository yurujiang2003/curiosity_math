from sympy import symbols, I, simplify

a = symbols('a')
b = a * (1 + I)
c = a * I

ac = a * c
b_squared = b**2
ab = a * b

expression = (ac + b_squared) / ab
final_result = simplify(expression)

final_result_simplified = final_result.simplify()
final_result_simplified
