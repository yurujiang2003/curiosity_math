from sympy import symbols, sqrt, simplify

l = symbols('l')
w = 13 - l
d = sqrt(l**2 + w**2)

diagonals = [d.subs(l, i).simplify() for i in range(1, 13)]
shortest_diagonal = min(diagonals)

shortest_diagonal
