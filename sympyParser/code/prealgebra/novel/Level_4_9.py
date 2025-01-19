from sympy import symbols, simplify

c = symbols('c')
jamie_spending = c + 3 * (c + 2)
kevin_spending = 5 * c
total_spending = simplify(jamie_spending + kevin_spending)

total_spending
