from sympy import symbols, Add

# Define the earnings in dollars
linda = 27.47
sherry = 35.23
june = 37.37
connie = 26.52

# Convert earnings to cents
linda_cents = linda * 100
sherry_cents = sherry * 100
june_cents = june * 100
connie_cents = connie * 100

# Calculate total earnings in cents
total_cents = Add(linda_cents, sherry_cents, june_cents, connie_cents)

# Calculate the remainder in cents after converting to dollars
remainder_cents = total_cents % 100

# Return the final answer
remainder_cents
