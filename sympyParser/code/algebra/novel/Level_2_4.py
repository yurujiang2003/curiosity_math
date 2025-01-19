from sympy import symbols, Eq, solve

x = symbols('x')
equation1 = Eq(4*x + 2, 10)
equation2 = Eq(4*x + 2, -10)

solution1 = solve(equation1, x)[0]
solution2 = solve(equation2, x)[0]

final_answer = solution2 if solution2 < 0 else None
final_answer
