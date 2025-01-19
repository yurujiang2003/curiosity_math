from sympy import symbols

n = symbols('n')
D = n * (n - 3) / 2

fifth_polygon_sides = 7
number_of_diagonals = D.subs(n, fifth_polygon_sides)

number_of_diagonals
