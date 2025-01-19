from sympy import Rational

# Total marbles in the jar
total_marbles = 28

# Number of red marbles
red_marbles = total_marbles / 2

# Number of non-red marbles
non_red_marbles = total_marbles - red_marbles

# Number of white marbles
white_marbles = non_red_marbles / 2

# Number of blue marbles
blue_marbles = non_red_marbles - white_marbles

# Total marbles after Todd chooses a white marble
remaining_white_marbles = white_marbles - 1
remaining_total_marbles = total_marbles - 1

# Probability that Hosea draws a white marble
probability_white = Rational(remaining_white_marbles, remaining_total_marbles)

# Final answer
probability_white.simplify()
