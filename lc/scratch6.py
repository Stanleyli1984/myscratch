__author__ = 'zhongqil'


import heapq

a = []
heapq.heappush(a, 2)
heapq.heappush(a, 1)
heapq.heappush(a, 3)

print a
heapq.heapify(a)
print a
print heapq.heappop(a)
print heapq.heappop(a)
print heapq.heappop(a)
