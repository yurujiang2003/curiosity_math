from sympy import symbols, S, prime

n = symbols('n', integer=True)
p_values = [prime(i) for i in range(1, 10)]  # Generate first few primes
solution = None

for p in p_values:
    n_value = (13 * p - 1) / (1 + p)
    if n_value.is_integer:
        solution = int(n_value)
        break

solution
