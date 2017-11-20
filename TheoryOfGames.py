from sympy import *


def simplex(a):
    m_min = 0
    m_ind = -1
    for j in range(1, 5):
        if a[2, j] < m_min and a[2, j] < 0:
            m_min = a[2, j]
            m_ind = j
    s_min = 100
    s_ind = -1
    for i in range(2):
        ss = a[i, 0] / a[i, m_ind]
        if ss < s_min:
            s_min = ss
            s_ind = i
        print(ss)

    a_cool = a[s_ind, m_ind]
    print(a_cool)
    a1 = a.copy()

    aij = a_cool
    for i in range(3):
        ai = a[i, m_ind]
        for j in range(5):
            if i != s_ind:
                a1[i, j] = a[i, j] - ai * a[s_ind, j] / aij
            else:
                a1[i, j] = a[i, j] / aij

    return a1


a = Matrix([
    [11, 3, 5, 1, 0],
    [8, 4, 1, 0, 1],
    [0, -8, -6, 0, 0]
])
pprint(a)
a2 = simplex(a)
pprint(a2)
a3 = simplex(a2)
a3 = a3.col_insert(5, Matrix([0, 0, 0]))
a3 = a3.row_insert(2, Matrix([[-Rational(12,17), 0, 0, -Rational(16,17), -Rational(5,17), 1]]))
pprint(a3)

