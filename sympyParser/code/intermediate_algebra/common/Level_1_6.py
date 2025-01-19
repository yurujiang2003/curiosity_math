from sympy import sqrt

a1, b1 = 10, -13
a2, b2 = 10, 13

magnitude1 = sqrt(a1**2 + b1**2)
magnitude2 = sqrt(a2**2 + b2**2)

result = magnitude1 * magnitude2
final_answer = result.evalf()

final_answer
