from sympy import log, Rational

a = log(5) / log(4)
b = log(6) / log(5)
c = log(7) / log(6)
d = log(8) / log(7)

result = a * b * c * d
final_answer = result.simplify()

final_answer
