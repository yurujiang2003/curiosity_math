from sympy import symbols, simplify

n = symbols('n')
sum_of_odds = n + (n + 2) + (n + 4) + (n + 6)
simplified_sum = simplify(sum_of_odds)
factored_sum = simplify(simplified_sum / 4)

final_answer = 4
final_answer
