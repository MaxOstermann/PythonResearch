from sympy import *
from math import *


def get_resh_col(a, n, m):
    m_min = 1000
    m_ind = 0
    for j in range(1, m):
        if a[n-1, j] <= m_min and a[n-1, j] < 0:
            m_min = a[n-1, j]
            m_ind = j
    return m_min, m_ind


def get_resh_col2(a, m, s_ind):
    m_min = 1000
    m_ind = 0
    print("m=", m)
    for j in range(1, m):
        if a[s_ind, j] <= m_min and a[s_ind, j] < 0:
            m_min = a[s_ind, j]
            m_ind = j
    return m_min, m_ind


def get_resh_row(a, n, m_ind):
    s_min = 100
    s_ind = -1000000
    for i in range(n - 1):
        ss = a[i, 0] / a[i, m_ind]
        if ss < s_min:
            #print(ss)
            s_min = ss
            s_ind = i
    return s_min, s_ind


def get_resh_row2(a, n):
    s_min = 100
    s_ind = -1000000
    for i in range(n - 1):
        ss = a[i, 0]
        if ss < s_min:
            print(ss)
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
                #print(a[i, j]," - ",ai," * ",a[s_ind, j]," / ",aij)
            else:
                a1[i, j] = a[i, j] / aij


    return a1


def simplex(a, n, m):
    m_min, m_ind = get_resh_col(a, n, m)
    s_min, s_ind = get_resh_row(a, n, m_ind)
    a1 = get_new_table(a, n, m, m_ind, s_ind)
    return a1


def simplex2(a, n, m):
    s_min, s_ind = get_resh_row2(a, n)
    m_min, m_ind = get_resh_col2(a, m, s_ind)
    a1 = get_new_table(a, n, m, m_ind, s_ind)
    return a1


# aa = Matrix([
#     [21, 5, 7, 1, 0],
#     [8, -1, 3, 0, 1],
#     [0, -1, -2, 0, 0]
# ])
aa = Matrix([
   [11, 3, 5, 1, 0],
   [8, 4, 1, 0, 1],
   [0, -8, -6, 0, 0]
])
xx = [1, 2]
pprint(aa)
a2 = simplex(aa, 3, 5)
pprint(a2)
a3 = simplex(a2, 3, 5)
pprint(a3)
a3 = a3.col_insert(5, Matrix([0, 0, 0]))
a3 = a3.row_insert(2, Matrix([[-Integer(12)/Integer(17), 0, 0, -Integer(16)/Integer(17), -Integer(5)/Integer(17), 1]]))
pprint(a3)
a4 = simplex2(a3, 4, 6)
print("lol")
pprint(a4)
a4 = a4.col_insert(6, Matrix([0, 0, 0, 0]))
a4 = a4.row_insert(3, Matrix([[-Integer(3)/Integer(4), 0, 0, 0, -Integer(5)/Integer(16), -Integer(15)/Integer(16), 1]]))
pprint(a4)
a5 = simplex2(a4, 5, 7)
pprint(a5)
a5 = a5.col_insert(7, Matrix([0, 0, 0, 0, 0]))
a5 = a5.row_insert(4, Matrix([[-Integer(4)/Integer(5), 0, 0, 0, -Integer(2)/Integer(3), 0, -Integer(4)/Integer(15), 1]]))
pprint(a5)
a6 = simplex2(a5, 6, 8)
pprint(a6)
a6 = a6.col_insert(8, Matrix([0, 0, 0, 0, 0, 0]))
a6 = a6.row_insert(5, Matrix([[-Integer(4)/Integer(5), 0, 0, 0, 0, 0, -Integer(3)/Integer(5), 0, 1]]))
pprint(a6)
a7 = simplex2(a6, 7, 9)
pprint(a7)
a7 = a7.col_insert(9, Matrix([0, 0, 0, 0, 0, 0, 0]))
a7 = a7.row_insert(6, Matrix([[-Integer(2)/Integer(3), 0, 0, 0, 0, 0, 0, -Integer(1)/Integer(2), -Integer(2)/Integer(3), 1]]))
pprint(a7)
a8 = simplex2(a7, 8, 10)
pprint(a8)