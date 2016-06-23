#use custom range for fuzzywuzzy and fcluster

import numpy as np
from scipy.cluster.hierarchy import fclusterdata
from fuzzywuzzy import fuzz
# a custom function that just computes Euclidean distance

dic = ['aaa', 'aaaa', 'abab', 'bbb', 'aa', 'bbbb']

def mydist(p1, p2):
    return 100 - fuzz.ratio(dic[int(p1[0])], dic[int(p2[0])])

#X = np.random.randn(10, 2)
X = np.array([[i] * 2 for i in xrange(len(dic))])

fclust1 = fclusterdata(X, 20, metric=mydist,criterion="distance")

#print(X)
print(fclust1)



# From So
# import numpy as np
# from scipy.cluster.hierarchy import fclusterdata
#
# # a custom function that just computes Euclidean distance
# def mydist(p1, p2):
#     diff = p1 - p2
#     return np.vdot(diff, diff) ** 0.5
#
# X = np.random.randn(100, 2)
#
# fclust1 = fclusterdata(X, 2, metric=mydist)
# fclust2 = fclusterdata(X, 2, metric='euclidean')
#
# print(fclust1, fclust2)
# print(np.allclose(fclust1, fclust2))
# # True