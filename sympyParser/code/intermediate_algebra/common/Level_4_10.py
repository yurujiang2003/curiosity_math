from sympy import symbols, solve, S, And, Or, Interval

x = symbols('x')

# Solve the first inequality: (x/(2*x - 1)) <= 3
inequality1 = (x / (2*x - 1)) - 3 <= 0
critical_points1 = [3/5, 1/2]
solution1 = solve(inequality1, x)

# Solve the second inequality: (x/(2*x - 1)) >= -3
inequality2 = (x / (2*x - 1)) + 3 >= 0
critical_points2 = [3/7, 1/2]
solution2 = solve(inequality2, x)

# Combine solutions
final_solution = Or(
    Interval.S.Reals.intersect(Interval(-S.Infinity, 1/2)),
    Interval(3/5, S.Infinity)
).intersect(
    Interval.S.Reals.intersect(Interval(1/2, 3/7))
)

final_solution
