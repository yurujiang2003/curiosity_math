from sympy import binomial, gcd, Rational

# Total number of ways to choose 3 cards from 52
total_ways = binomial(52, 3)

# Number of ways to form a hand with a pair
ways_to_form_pair = binomial(13, 1) * binomial(4, 2) * binomial(48, 1)

# Probability of drawing a pair
probability_pair = Rational(ways_to_form_pair, total_ways)

# Simplifying the fraction
numerator = ways_to_form_pair
denominator = total_ways
gcd_value = gcd(numerator, denominator)

final_numerator = numerator // gcd_value
final_denominator = denominator // gcd_value

final_probability = Rational(final_numerator, final_denominator)

final_probability
