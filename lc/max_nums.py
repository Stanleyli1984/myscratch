__author__ = 'zhongqil'

import heapq
def func(l, max_num):
    h = []
    for i in xrange(max_num):
        heapq.heappush(h, l[i])
        print h
    for i in xrange(max_num, len(l)):
        if l[i] > h[0]:
            heapq.heappop(h)
            heapq.heappush(h, l[i])
        print h
    print h

func([6,5,3,4,1,100], 3)