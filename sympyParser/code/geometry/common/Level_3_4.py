from sympy import symbols, sqrt, Min

l = symbols('l')
w = 13 - l
d = sqrt(l**2 + w**2)

diagonal_lengths = [d.subs(l, i) for i in range(1, 13)]
shortest_diagonal = Min(*diagonal_lengths)

shortest_diagonal
