import math

def eigen(p_matrix, a, epsilon):
    q = []

    q = p_matrix
    p = AxP(a, p_matrix)
    l = norm(p)
    p = PxL(p, 1/l)

    while norm(PminusQ(p,q)) > epsilon:
        print("her")
        q = p
        p = AxP(a, p)
        l = norm(p)
        p = PxL(p, 1 / l)

    print(str(p))
    print("Lambda: " + str(l))

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

if __name__ == '__main__':
    epsilon = 0.0000001
    a = [[0, 1, 1, 0, 0, 1],
         [1, 0, 1, 0, 1, 0],
         [1, 1, 0, 1, 1, 1],
         [0, 0, 1, 0, 1, 1],
         [0, 1, 1, 1, 0, 0],
         [1, 0, 1, 1, 0, 0]]

    p = [3, 3, 5, 3, 3, 3]
    eigen(p, a, epsilon)
    # graph = [set() for _ in range(6)]
    # # edges = [[0, 1],
    # # [0, 2],
    # # [1, 2],
    # # [1, 3],
    # # [1, 4],
    # # [2, 4],
    # # [3, 4],
    # # [3, 5],
    # # [3, 6],
    # # [4, 6],
    # # [4, 7],
    # # [5, 8],
    # # [5, 9],
    # # [6, 9],
    # # [7, 9],
    # # [8, 9]]
    # edges = [[0,1],[0,2],[0,5],[1,2],[1,4],[2,3],[2,5],[3,4],[4,1],[4,2],[5,3]]
    #
    # for i in edges:
    #     graph[i[0]].add(i[1])
    #     graph[i[1]].add(i[0])
    #
    # total = [0] * 6
    #
    # for i in range(6):
    #     for j in range(6):
    #         if i != j:
    #             paths = bfs_paths(graph, i, j)
    #
    #             counter = [0] * 6
    #             for row in paths:
    #                 for k in range(6):
    #                     if k != i and k != j and k in row:
    #                         counter[k] += 1
    #
    #             for node in range(6):
    #                 total[node] += counter[node] / len(paths)
    #
    # for i in total:
    #     print(i/2)
    #             # print("New bfs")
    #             # for row in paths:
    #             #     print(str(row))