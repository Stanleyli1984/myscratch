# Definition for an interval.
class Interval:
     def __init__(self, s=0, e=0):
         self.start = s
         self.end = e

class Solution:
    # @param {Interval[]} intervals
    # @param {Interval} newInterval
    # @return {Interval[]}
    def insert(self, intervals, newInterval):
        if not intervals:
            return [newInterval]
        intervals = sorted(intervals, key=lambda x:x.start)

        affected = []
        for idx, interval in enumerate(intervals):
            if not (interval.start > newInterval.end or interval.end < newInterval.start):
                affected.append(idx)

        if not affected:
            return sorted(intervals + [newInterval], key=lambda x:x.start)
        else:
            return intervals[:affected[0]] + [Interval(min(intervals[affected[0]].start, newInterval.start), max(intervals[affected[-1]].end, newInterval.end))] + \
                 intervals[affected[-1]+1:]

r = Solution().insert([Interval(1,2), Interval(4,5)], Interval(2,7))
a = 1


