from sympy import N, round

# Define the costs of the items
cake_cost = 17.86
apples_cost = 7.46
celery_cost = 8.66

# Round each cost to the nearest dollar
rounded_cake = round(cake_cost)
rounded_apples = round(apples_cost)
rounded_celery = round(celery_cost)

# Calculate the total approximate cost
total_cost = rounded_cake + rounded_apples + rounded_celery

# Determine the closest answer choice
answer = 'C' if total_cost == 34 else None

answer
