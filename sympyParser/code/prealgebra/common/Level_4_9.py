from sympy import symbols, simplify

c = symbols('c')

# Cost calculations
cost_chocolate = c
cost_vanilla = c + 2

# Jamie's total cost
jamie_total = cost_chocolate + 3 * cost_vanilla

# Kevin's total cost
kevin_total = 5 * cost_chocolate

# Total spent by both
total_spent = simplify(jamie_total + kevin_total)

total_spent
