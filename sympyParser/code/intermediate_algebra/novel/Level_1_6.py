from sympy import sqrt

a = 10
b1 = -13
b2 = 13

magnitude1 = sqrt(a**2 + b1**2)
magnitude2 = sqrt(a**2 + b2**2)

result = magnitude1 * magnitude2
final_answer = result.evalf()

final_answer
