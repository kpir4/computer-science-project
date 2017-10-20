import math
from numpy import save, load
import db_manager

def eigenvector(p_matrix, a, epsilon):
    dbu = db_manager.DatabaseUtility()
    employee_data = dbu.get_eid()

    q = p_matrix
    p = AxP(a, p_matrix)
    l = norm(p)
    p = PxL(p, 1/l)

    while norm(PminusQ(p,q)) > epsilon:
        q = p
        p = AxP(a, p)
        l = norm(p)
        p = PxL(p, 1 / l)

    for node in range(len(p)):
        label = employee_data[node][1] + ' ' + employee_data[node][2]
        p[node] = (label, p[node], node)

    p.sort(key = lambda x: x[1], reverse = True)

    return p

def AxP(a, p):
    q = [None] * len(p)

    for i in range(len(p)):
        q[i] = 0
        for j in range(len(p)):
            q[i] = q[i] + a[i][j] * p[j]

    return q

def PxL(p, l):
    q = [None] * len(p)

    for i in range(len(p)):
        q[i] = p[i] * l

    return q

def PminusQ(p, q):
    r = [None] * len(p)
    for i in range(len(p)):
        r[i] = p[i] - q[i]

    return r

def norm(p):
    s = 0

    for i in range(len(p)):
        s += p[i] * p[i]
    return math.sqrt(s)