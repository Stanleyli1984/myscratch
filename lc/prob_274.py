class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """

        array = [0] * len(citations)
        for citation in citations:
            if citation == 0:
                continue
            if citation >= len(citations):
                array[-1] += 1
            else:
                array[citation-1] += 1
        result = 0
        current_sum = 0
        for idx in reversed(xrange(0, len(array))):
            current_sum = current_sum + array[idx]
            min_n = min(current_sum, idx + 1)
            result = min_n if min_n > result else result
        return result

print Solution().hIndex([0])