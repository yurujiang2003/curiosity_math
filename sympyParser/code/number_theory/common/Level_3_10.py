from sympy import symbols, mod

a = 11
r = 11
n = 9

S = a * (r**n - 1) / (r - 1)
S = (11**10 - 11) / 10

S_mod_100 = S.subs(11**10, 1) % 100
tens_digit = S_mod_100 // 10

tens_digit
