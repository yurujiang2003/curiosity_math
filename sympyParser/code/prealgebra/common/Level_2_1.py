from sympy import symbols, Rational, solve, S

x = symbols('x')
inequality1 = Rational(3, 5) < x / 7
inequality2 = x / 7 < Rational(7, 9)

solution1 = solve(inequality1, x)
solution2 = solve(inequality2, x)

final_solution = S.Integers.intersect(solution1, solution2)
result = [sol for sol in final_solution if sol.is_integer]

result
