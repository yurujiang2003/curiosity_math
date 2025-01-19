from sympy import Rational

# Define the number of red and blue marbles
red_marbles = 4
blue_marbles = 6
total_marbles = red_marbles + blue_marbles

# Probability of drawing two red marbles
P_first_red = Rational(red_marbles, total_marbles)
P_second_red_given_first = Rational(red_marbles - 1, total_marbles - 1)
P_both_red = P_first_red * P_second_red_given_first

# Probability of drawing two blue marbles
P_first_blue = Rational(blue_marbles, total_marbles)
P_second_blue_given_first = Rational(blue_marbles - 1, total_marbles - 1)
P_both_blue = P_first_blue * P_second_blue_given_first

# Total probability of both marbles being the same color
P_same_color = P_both_red + P_both_blue

# Return the final answer
P_same_color
