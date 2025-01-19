from sympy import symbols, Mod

k = symbols('k')
N = 8 * k + 7
left_over = Mod(N, 4).subs(k, 0)  # Substitute k with 0 to find the remainder
left_over
