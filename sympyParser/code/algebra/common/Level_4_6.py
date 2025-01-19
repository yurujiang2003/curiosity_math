from sympy import symbols, Rational

n = 15
denominator = n + 1
sum_of_n = n * (n + 1) // 2
sum_fractions = Rational(sum_of_n, denominator)
sum_fractions.evalf()
