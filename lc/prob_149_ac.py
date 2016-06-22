# Definition for a point
# class Point:
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b
from collections import Counter
class Solution:
    # @param points, a list of Points
    # @return an integer

    def maxPoints(self, points):
        max_points = 0
        if len(points) == 1:
            return 1
        for i, point in enumerate(points):
            slope_lists = []
            overlap  = 0
            num_most_common = 0
            for j, inner_point in enumerate(points[i+1:]):
                if inner_point.x - point.x == 0:
                    if inner_point.y - point.y == 0:
                        overlap += 1
                    else:
                        slope_lists.append('inf')
                else:
                    slope_lists.append((float)(inner_point.y - point.y)/(inner_point.x - point.x))
            if slope_lists:
                most_common,num_most_common = Counter(slope_lists).most_common(1)[0]
            max_points = max(max_points, num_most_common + 1 + overlap)
        return max_points