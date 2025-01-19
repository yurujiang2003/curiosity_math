from sympy import symbols, Rational

BD = 5
CD = 9
CE = Rational(42, 5)

BC = BD + CD
HE = CE * (BD / BC)

HE.evalf()
