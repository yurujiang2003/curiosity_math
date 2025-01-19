from sympy import symbols, floor

n = 20
multiples_of_3 = floor((n - 1) / 3)
multiples_of_6 = floor((n - 1) / 6)

result = multiples_of_6 - multiples_of_3
result
