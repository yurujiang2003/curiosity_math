from sympy import symbols, factorint, isprime

n_limit = 10000
m_limit = n_limit + 2005
valid_n = []

for p1 in range(2, 100):
    if isprime(p1):
        for p2 in range(2, 100):
            if isprime(p2) and p1 != p2:
                m1 = p1**2 * p2**6
                if m1 < m_limit:
                    n1 = m1 - 2005
                    if n1 > 0:
                        valid_n.append(n1)

                m2 = p2**2 * p1**6
                if m2 < m_limit:
                    n2 = m2 - 2005
                    if n2 > 0:
                        valid_n.append(n2)

result = sum(set(valid_n))
result
