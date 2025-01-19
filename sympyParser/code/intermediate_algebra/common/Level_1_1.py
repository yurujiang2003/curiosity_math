from sympy import log, Rational

# Calculate log_2(256)
log2_256 = log(256, 2)

# Calculate log_8(64)
log2_64 = log(64, 2)
log2_8 = log(8, 2)
log8_64 = log2_64 / log2_8

# Calculate log_(log_8(64))(256)
final_result = log(256, log8_64)

final_result
