from sympy import symbols, summation, fibonacci, oo, limit

n = symbols('n')
S = summation(1/(fibonacci(n)*fibonacci(n + 2)), (n, 1, oo))
result = limit(S, n, oo)
final_answer = 1 - result
final_answer
