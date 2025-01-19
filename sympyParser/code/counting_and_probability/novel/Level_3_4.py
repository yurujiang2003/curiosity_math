from sympy import Rational

# Define the number of red and blue marbles
red_marbles = 4
blue_marbles = 6
total_marbles = red_marbles + blue_marbles

# Step 1: Probability of drawing two red marbles
P_Red1 = Rational(red_marbles, total_marbles)
P_Red2_given_Red1 = Rational(red_marbles - 1, total_marbles - 1)
P_Both_Red = P_Red1 * P_Red2_given_Red1

# Step 2: Probability of drawing two blue marbles
P_Blue1 = Rational(blue_marbles, total_marbles)
P_Blue2_given_Blue1 = Rational(blue_marbles - 1, total_marbles - 1)
P_Both_Blue = P_Blue1 * P_Blue2_given_Blue1

# Step 3: Total probability of drawing two marbles of the same color
P_Same_Color = P_Both_Red + P_Both_Blue

# Return the final answer
P_Same_Color
