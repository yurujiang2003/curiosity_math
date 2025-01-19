from sympy import Rational

total_marbles = 28
red_marbles = total_marbles / 2
non_red_marbles = total_marbles - red_marbles
white_marbles = non_red_marbles / 2
blue_marbles = non_red_marbles - white_marbles

remaining_white_marbles = white_marbles - 1
total_remaining_marbles = red_marbles + remaining_white_marbles + blue_marbles

probability_white = Rational(remaining_white_marbles, total_remaining_marbles).simplify()
probability_white
