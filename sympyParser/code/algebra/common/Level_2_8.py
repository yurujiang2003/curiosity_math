from sympy import symbols, Eq, solve, sum

n = symbols('n')
equation = Eq(n + (n + 1) + (n + 2) + (n + 3), 22)
solution = solve(equation, n)[0]

integers = [solution + i for i in range(4)]
new_integers = [x + 2 for x in integers]
multiplied_integers = [x * 20 for x in new_integers]
final_sum = sum(multiplied_integers)

final_sum
