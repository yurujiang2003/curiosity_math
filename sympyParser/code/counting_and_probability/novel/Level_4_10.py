from sympy import Rational

# Define probabilities
P_W = Rational(1, 5)  # Probability of selecting the white ball from Bin A
P_B = Rational(4, 5)  # Probability of selecting a black ball from Bin A

# Expected value from Bin B
E_B = (Rational(3, 4) * 1) + (Rational(1, 4) * 7)

# Expected value from Bin W
E_W = (Rational(5, 6) * 8) + (Rational(1, 6) * 500)

# Overall expected win
E = (P_B * E_B) + (P_W * E_W)

E
