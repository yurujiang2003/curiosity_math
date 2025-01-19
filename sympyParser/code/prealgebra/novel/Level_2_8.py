from sympy import isprime, symbols, Sum

start, end = 10, 20
composite_numbers = [n for n in range(start + 1, end) if not isprime(n)]
result = Sum(composite_numbers).doit()
result
