from sympy import *


def get_resh_col(a, n, m):
    m_min = 1000
    m_ind = 0
    for j in range(1, m):
        if a[n-1, j] <= m_min and a[n-1, j] < 0:
            m_min = a[n-1, j]
            m_ind = j
    return m_min, m_ind


def get_resh_row(a, n, m_ind):
    s_min = 100
    s_ind = -1
    for i in range(n - 1):
        ss = a[i, 0] / a[i, m_ind]
        if ss < s_min:
            s_min = ss
            s_ind = i
    return s_min, s_ind


def get_new_table(a, n, m, m_ind, s_ind):
    a_cool = a[s_ind, m_ind]
    print(a_cool)
    a1 = a.copy()

    aij = a_cool
    for i in range(n):
        ai = a[i, m_ind]
        for j in range(m):
            if i != s_ind:
                a1[i, j] = a[i, j] - ai * a[s_ind, j] / aij
            else:
                a1[i, j] = a[i, j] / aij

    return a1


def simplex(a, n, m):
    m_min, m_ind = get_resh_col(a, n, m)
    s_min, s_ind = get_resh_row(a, n, m_ind)
    a1 = get_new_table(a, n, m, m_ind, s_ind)
    return a1


aa = Matrix([
    [11, 3, 5, 1, 0],
    [8, 4, 1, 0, 1],
    [0, -8, -6, 0, 0]
])
pprint(aa)
a2 = simplex(aa, 3, 5)
pprint(a2)
a3 = simplex(a2, 3, 5)
pprint(a3)
#a3 = a3.col_insert(5, Matrix([0, 0, 0]))
#a3 = a3.row_insert(2, Matrix([[-Integer(12)/Integer(17), 0, 0, -Integer(16)/Integer(17), -Integer(5)/Integer(17), 1]]))
#pprint(a3)
#a4 = simplex(a3, 4, 6)
#print("lol")

#pprint(a4)