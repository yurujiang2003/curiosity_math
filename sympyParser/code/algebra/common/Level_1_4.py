from sympy import Rational

numerator = Rational(3, 8) + Rational(7, 8)
simplified_numerator = numerator.simplify()
denominator = Rational(4, 5)
result = simplified_numerator / denominator
final_answer = result.simplify()
final_answer
