from sympy import binomial, Rational

# Define probabilities for Coin A
P_HA_0 = binomial(3, 0) * (1/2)**3
P_HA_1 = binomial(3, 1) * (1/2)**3
P_HA_2 = binomial(3, 2) * (1/2)**3
P_HA_3 = binomial(3, 3) * (1/2)**3

# Define probabilities for Coin B
P_HB_0 = binomial(2, 0) * (1/2)**2
P_HB_1 = binomial(2, 1) * (1/2)**2
P_HB_2 = binomial(2, 2) * (1/2)**2

# Calculate probabilities for H_A > H_B
probability = (
    P_HA_1 * P_HB_0 +
    P_HA_2 * P_HB_0 +
    P_HA_2 * P_HB_1 +
    P_HA_3 * P_HB_0 +
    P_HA_3 * P_HB_1 +
    P_HA_3 * P_HB_2
)

# Return the final answer as a common fraction
final_answer = Rational(probability).simplify()
final_answer
