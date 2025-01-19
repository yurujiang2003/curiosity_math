from sympy import binomial, Mod

n = 9
a = 11
r = 11

S_n = a * (r**n - 1) / (r - 1)

# Calculate 11^9 using binomial expansion
power = sum(binomial(n, k) * 10**k for k in range(n + 1))

# Calculate 11^9 mod 100
last_two_digits = Mod(power, 100)

# Calculate the sum S_9
S_9 = a * (last_two_digits - 1) / 10

# Get the tens digit
tens_digit = int(S_9) // 10 % 10

tens_digit
