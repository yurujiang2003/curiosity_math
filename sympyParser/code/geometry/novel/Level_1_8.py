from sympy import symbols, Rational

BC = 6  # length of side BC in inches
DE = Rational(1, 2) * BC  # length of segment DE using the Midsegment Theorem
DE.evalf()  # evaluate to get the numerical result
