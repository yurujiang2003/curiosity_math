from sympy import symbols, simplify

a, b, c = 1990, 1000, 990

sum_abc = a + b + c
ab = a * b
ac = a * c
bc = b * c
ab_ac_bc = ab + ac + bc

a2 = a**2
b2 = b**2
c2 = c**2
sum_a2_b2_c2 = a2 + b2 + c2

result = sum_a2_b2_c2 - ab_ac_bc
final_expression = (sum_abc * result + 3 * ab * ac) / (a * b * c)

final_answer = simplify(final_expression)
final_answer
