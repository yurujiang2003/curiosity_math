from sympy import binomial, Rational

n = 3  # number of friends
k = 2  # number of friends born on Tuesday
p = Rational(1, 7)  # probability of being born on Tuesday

# Calculate the probability
probability = binomial(n, k) * p**k * (1 - p)**(n - k)
final_answer = probability.simplify()

final_answer
