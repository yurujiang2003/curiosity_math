from sympy import symbols, Rational

# Given values
BD = 5
CD = 9
CE = Rational(42, 5)

# Calculate BC
BC = BD + CD

# Calculate BE using the property of segments
BE = (BD / CD) * CE

# Calculate HE using the relationship between segments
HE = (BE * CE) / BC

# Simplify HE
HE_simplified = HE.simplify()

HE_simplified
