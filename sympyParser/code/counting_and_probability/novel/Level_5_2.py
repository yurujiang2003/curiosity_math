from sympy import binomial, gcd, Rational

# Total number of peppers
total_peppers = 10 + 5

# Total ways to select 6 peppers from 15
total_ways = binomial(total_peppers, 6)

# Case 1: 4 green peppers and 2 red peppers
ways_case_1 = binomial(5, 4) * binomial(10, 2)

# Case 2: 5 green peppers and 1 red pepper
ways_case_2 = binomial(5, 5) * binomial(10, 1)

# Case 3: 6 green peppers and 0 red peppers
ways_case_3 = 0

# Total favorable outcomes
total_favorable = ways_case_1 + ways_case_2 + ways_case_3

# Calculate the probability
probability = Rational(total_favorable, total_ways)

# Simplify the fraction
final_numerator = probability.p * (1 if probability.q == 1 else gcd(probability.p, probability.q))
final_denominator = probability.q * (1 if probability.p == 1 else gcd(probability.p, probability.q))

final_answer = Rational(final_numerator, final_denominator)

final_answer
