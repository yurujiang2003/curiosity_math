from sympy import symbols, Eq, solve

A, M, C = symbols('A M C')

equation = Eq(100*A + 10*M + C, 617)
solutions = []

for a in range(1, 10):
    equation_substituted = equation.subs(A, a)
    result = solve(equation_substituted, (M, C))
    for m, c in result:
        if 0 <= m < 10 and 0 <= c < 10:
            solutions.append((a, m, c))

A, M, C = solutions[0]  # Only valid solution
final_answer = A + M + C
final_answer
