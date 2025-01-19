from sympy import symbols, Eq, solve

A, M, C = symbols('A M C')
equation = Eq(100*A + 10*M + C, 617)

solutions = []
for m in range(2):  # M can be 0 or 1
    c = 17 - 10*m
    if 0 <= c <= 9:
        solutions.append((6, m, c))

final_answer = sum(solutions[0])  # Only one valid solution
final_answer
