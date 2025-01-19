from sympy import Rational

hockey_shirts = 3
football_shirts = 2
baseball_shirts = 7

total_shirts = hockey_shirts + football_shirts + baseball_shirts
non_baseball_shirts = hockey_shirts + football_shirts

probability_not_baseball = Rational(non_baseball_shirts, total_shirts)
probability_not_baseball
