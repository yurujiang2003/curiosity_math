from sympy import symbols, Rational

# Define variables
original_price = 60
discount_rate = Rational(20, 100)
commission_rate = Rational(5, 100)

# Calculate commission on original price
commission_original = commission_rate * original_price

# Calculate price after discount
discount_amount = discount_rate * original_price
price_after_discount = original_price - discount_amount

# Calculate commission on discounted price
commission_discounted = commission_rate * price_after_discount

# Determine the difference in commission
difference = commission_original - commission_discounted

# Convert difference to cents
difference_cents = difference * 100

# Return the final answer
difference_cents
