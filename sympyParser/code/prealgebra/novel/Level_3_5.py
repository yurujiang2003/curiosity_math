from sympy import Rational

# Define the number of face cards and total cards
face_cards = 3 * 4  # 3 face cards per suit and 4 suits
total_cards = 52

# Calculate the probability
probability = Rational(face_cards, total_cards)

# Return the final answer
probability
