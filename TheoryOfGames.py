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
            else:
                a1[i, j] = a[i, j] / aij


    return a1


def add_cond(a, n, m):
    max_value = 0
    val = 0
    st = 0
    for i in range(n):
        if a[i, 0]-floor(a[i, 0]) > max_value:
            max_value = a[i, 0]-floor(a[i, 0])
            val = a[i,0]
            st = i
    print(max_value, val)
    aa =  Matrix([0])
    for i in range(1, n):
        aa = aa.row_insert(i, Matrix([[0]]))
    pprint(aa)
    aaa = Matrix([-max_value])
    for i in range(1, m):
        aaa = aaa.col_insert(i, Matrix([-1*(a[st, i]-floor(a[st, i]))]))
    aaa = aaa.col_insert(m, Matrix([1]))
    pprint(aaa)
    aaaa = a.col_insert(m, aa)
    aaaa = aaaa.row_insert(n-1, aaa)
    return  aaaa

def simplex(a, n, m):
    m_min, m_ind = get_resh_col(a, n, m)
    s_min, s_ind = get_resh_row(a, n, m_ind)
    a1 = get_new_table(a, n, m, m_ind, s_ind)
    return a1, m_ind, s_ind


def simplex2(a, n, m):
    s_min, s_ind = get_resh_row2(a, n)
    m_min, m_ind = get_resh_col2(a, m, s_ind)
    a1 = get_new_table(a, n, m, m_ind, s_ind)
    return a1, m_ind, s_ind


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
xx = [3, 4]
pprint(aa)
m_ind=-1
s_ind=-1
a2, m_ind, s_ind = simplex(aa, 3, 5)
xx[s_ind] = m_ind
pprint(a2)
print(xx)
a3, m_ind, s_ind = simplex(a2, 3, 5)

xx[s_ind] = m_ind
pprint(a3)
a3 = add_cond(a3, 3, 5)
xx.append(1)
pprint(a3)
a4, m_ind, s_ind = simplex2(a3, 4, 6)
xx[s_ind] = m_ind
print("lol")
pprint(a4)
a4 = add_cond(a4, 4, 6)
xx.append(1)
pprint(a4)
a5, m_ind, s_ind = simplex2(a4, 5, 7)
xx[s_ind] = m_ind
pprint(a5)
a5 = add_cond(a5, 5, 7)
xx.append(1)
pprint(a5)
a6, m_ind, s_ind = simplex2(a5, 6, 8)
xx[s_ind] = m_ind
pprint(a6)
a6 = add_cond(a6, 6, 8)
xx.append(1)
pprint(a6)
a7, m_ind, s_ind = simplex2(a6, 7, 9)
xx[s_ind] = m_ind
pprint(a7)
print('add_cond = ',add_cond(a7, 7, 9))
a7 = add_cond(a7, 7, 9)
xx.append(1)
pprint(a7)
print(xx)
a8, m_ind, s_ind = simplex2(a7, 8, 10)
xx[s_ind] = m_ind
pprint(a8)
print(xx)
for i in range(len(xx)):
    print("x",xx[i],"=",a8[i,0])