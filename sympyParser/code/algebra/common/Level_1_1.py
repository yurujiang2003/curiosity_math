from sympy import symbols, Sum, oo

n = symbols('n')
odd_integers = [2*i + 1 for i in range(5)]
sum_of_odds = Sum(odd_integers).doit()
sum_of_odds
