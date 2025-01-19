from sympy import Rational

# Define the number of face cards and total cards
num_face_cards = 3 * 4
total_cards = 52

# Calculate the probability
probability = Rational(num_face_cards, total_cards)

# Return the final answer
probability
