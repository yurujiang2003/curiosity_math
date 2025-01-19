from sympy import symbols, solve, tan

k = symbols('k')
n = 252 + k * 180
solution = solve(-90 < n, k)

valid_n = [n.subs(k, val) for val in solution if -90 < n.subs(k, val) < 90]
final_answer = valid_n[0] if valid_n else None
final_answer
