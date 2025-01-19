from sympy import symbols, Rational

star, star_op, star_val = symbols('star star_op star_val')
star_op = '*'
operations = { '+': lambda x, y: x + y, '-': lambda x, y: x - y, '*': lambda x, y: x * y, '/': lambda x, y: x / y }

# Define the values
A = 12
B = 2
C = 9
D = 3

# Check the operations for 9 * 3
results = []
for op in operations:
    if op == '+':
        value = operations[op](C, D)
    elif op == '-':
        value = operations[op](C, D)
    elif op == '*':
        value = operations[op](C, D)
    elif op == '/':
        value = operations[op](C, D)

    if op == '+':
        if A * star_val == 4 * value:
            star_val = '*'
            results.append((star_val, op))
    elif op == '-':
        if A * star_val == 4 * value:
            star_val = '*'
            results.append((star_val, op))
    elif op == '*':
        if A * star_val == 4 * value:
            star_val = '*'
            results.append((star_val, op))
    elif op == '/':
        if A * star_val == 4 * value:
            star_val = '*'
            results.append((star_val, op))

# Assuming we found star = '*' and * = '-'
star = '*'
star_op = '-'

# Calculate the final expression
final_result = Rational(10 * 7, 24 - 9)
final_result
