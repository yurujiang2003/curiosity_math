from sympy import symbols, solve, S, Interval

x = symbols('x')
inequality1 = x / (2*x - 1) - 3
inequality2 = x / (2*x - 1) + 3

solution1 = solve(inequality1 <= 0, x)
solution2 = solve(inequality2 >= 0, x)

result1 = Interval(solution1[0], S.Infinity)
result2 = Interval(solution2[0], S.Infinity)

final_solution = result1.intersect(result2).remove(Interval(1/2, 1/2))
final_solution
