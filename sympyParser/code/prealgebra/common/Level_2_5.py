from sympy import N

cake_price = 17.86
apples_price = 7.46
celery_price = 8.66

rounded_cake = round(cake_price)
rounded_apples = round(apples_price)
rounded_celery = round(celery_price)

total_cost = rounded_cake + rounded_apples + rounded_celery

options = {
    'A': 50,
    'B': 38,
    'C': 34,
    'D': 26,
    'E': 20
}

closest_option = min(options, key=lambda x: abs(options[x] - total_cost))

closest_option
