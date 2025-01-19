from sympy import symbols, N

A = 100000
r = 0.06
t = 5

P = A / (1 + r)**t
final_amount = N(P).round()

final_amount
