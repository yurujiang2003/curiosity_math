from sympy import divisors

m_candidates = divisors(80)
not_divisors_of_8 = [d for d in m_candidates if d not in divisors(8)]
result = len(not_divisors_of_8)
result
