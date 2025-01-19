from sympy import binomial, Rational

# Define probabilities for coin A
P_A = [binomial(3, k) * Rational(1, 8) for k in range(4)]  # P(X_A = 0, 1, 2, 3)

# Define probabilities for coin B
P_B = [binomial(2, k) * Rational(1, 4) for k in range(3)]  # P(X_B = 0, 1, 2)

# Calculate the probability that X_A > X_B
probability = (
    P_A[1] * P_B[0] +  # P(X_A = 1, X_B = 0)
    P_A[2] * P_B[0] +  # P(X_A = 2, X_B = 0)
    P_A[2] * P_B[1] +  # P(X_A = 2, X_B = 1)
    P_A[3] * P_B[0] +  # P(X_A = 3, X_B = 0)
    P_A[3] * P_B[1] +  # P(X_A = 3, X_B = 1)
    P_A[3] * P_B[2]    # P(X_A = 3, X_B = 2)
)

# Return the final answer
probability
