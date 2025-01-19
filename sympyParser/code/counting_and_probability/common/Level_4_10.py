from sympy import Rational

# Step 1: Probabilities from bin A
P_W = Rational(1, 5)
P_B = Rational(4, 5)

# Step 2: Expected win from bin W
E_W = (Rational(5, 6) * 8) + (Rational(1, 6) * 500)

# Expected win from bin B
E_B = (Rational(3, 4) * 1) + (Rational(1, 4) * 7)

# Step 3: Overall expected win
E = (P_W * E_W) + (P_B * E_B)

E.evalf()
