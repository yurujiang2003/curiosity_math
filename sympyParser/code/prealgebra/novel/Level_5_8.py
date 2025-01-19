from sympy import symbols, Rational

# Define variables
original_price = 60
discount_rate = Rational(20, 100)
commission_rate = Rational(5, 100)

# Calculate original commission
original_commission = commission_rate * original_price * 100  # in cents

# Calculate discounted price
discount_amount = discount_rate * original_price
discounted_price = original_price - discount_amount

# Calculate commission on discounted price
discounted_commission = commission_rate * discounted_price * 100  # in cents

# Calculate the difference in commission
difference_in_commission = original_commission - discounted_commission

# Return the final answer
difference_in_commission
