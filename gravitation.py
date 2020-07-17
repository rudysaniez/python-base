#########################
# Gravitation
#########################

def gravitation(m_x, m_y, distance):
    return 6.67 * 10 ** -11 * ((m_x * m_y) / distance ** 2)


g = gravitation(10000, 10000, 0.05)
print(g)
