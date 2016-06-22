__author__ = 'zhongqil'

def func(M, K):
    distances = set()
    edges = set()
    for i in xrange(len(M)):
        for j in xrange(len(M[0])):
            if M[i][j] == 1:
                distances.add((i, j))
                edges.add((i, j))
    for k in xrange(K-1):
            new_edges = set()
            for x, y in edges:
                for i, j in ((x-1, y),(x+1, y),(x, y-1), (x, y+1)):
                    try:
                        _ = M[i][j]
                        if (i, j) not in distances:
                            distances.add((i,j))
                            new_edges.add((i,j))
                    except IndexError:
                        pass
            edges = set(new_edges)
    new_M = [[0] * len(M[0]) for _ in xrange(len(M))]
    for i in xrange(len(M)):
        for j in xrange(len(M[0])):
            new_M[i][j] = 1 if (i,j) in distances else 0
    print new_M

func([[0,0,0,0,0], [0,0,0,0,0], [0,1,1,0,0], [0,0,0,0,0], [0,0,0,0,0]], 2)








