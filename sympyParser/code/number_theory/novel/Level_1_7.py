from sympy import symbols, Mod

k = symbols('k')
N = 8 * k + 7
left_over = Mod(N, 4).simplify()
final_answer = left_over.subs(k, 0)  # Substitute k=0 to find the remainder
final_answer
