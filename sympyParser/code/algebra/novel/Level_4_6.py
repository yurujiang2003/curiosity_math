from sympy import symbols, Rational

n = 15
denominator = n + 1
sum_of_integers = n * (n + 1) // 2
S = Rational(sum_of_integers, denominator)
S.evalf()
