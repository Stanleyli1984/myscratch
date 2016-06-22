# Definition for an interval.
class Interval:
     def __init__(self, s=0, e=0):
         self.start = s
         self.end = e

class Solution:
    # @param {Interval[]} intervals
    # @return {Interval[]}
    def merge(self, intervals):
        if not intervals:
            return []
        intervals = sorted(intervals, key=lambda x:x.start)
        idx = 0
        results = []
        start = intervals[0].start
        end = intervals[0].end
        while(idx < len(intervals)):
            anchor = intervals[idx].start
            while idx < len(intervals) and intervals[idx].start == anchor:
                if intervals[idx].end > end:
                    end = intervals[idx].end
                idx += 1
            if idx == len(intervals) or intervals[idx].start > end:
                results.append(Interval(start, end))
                if idx < len(intervals):
                    start = intervals[idx].start
        return results


a = [Interval(1,2), Interval(3,4)]
Solution().merge(a)


