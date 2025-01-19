from sympy import symbols, solve, Rational

r = symbols('r')
k1 = 1
k2 = Rational(1, 2)
k3 = Rational(1, 3)
k4 = 1/r

left_side = (k1 + k2 + k3 + k4)**2
right_side = 2 * (k1**2 + k2**2 + k3**2 + k4**2)

equation = left_side - right_side
solution = solve(equation, r)

final_answer = [sol.evalf() for sol in solution if sol > 0]
final_answer
