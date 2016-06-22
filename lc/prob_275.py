class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        satisfy = lambda idx: citations[idx] >= len(citations) - idx
        if not citations:
            return 0
        start = 0
        end = len(citations) - 1
        while True:
            if start == end:
                if satisfy(start) == 0:
                    return len(citations) - start - 1
                else:
                    return len(citations) - start
            mid = (start + end) / 2
            if satisfy(mid):
                end = mid
            else:
                start = mid + 1

print Solution().hIndex([1,1,1,2])