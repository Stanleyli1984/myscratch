__author__ = 'zhongqil'

class Solution:
    # @param {integer[]} nums
    # @return {string[]}
    def summaryRanges(self, nums):
        ranges = []
        results = []
        prev = None
        if not nums:
            return []
        start = nums[0]
        for num in nums:
            if prev is not None and num != prev + 1:
                ranges.append((start, prev))
                start = num
            prev = num
        ranges.append((start, nums[-1]))
        for start, end in ranges:
            if start == end:
                results.append(str(start))
            else:
                results.append("%s->%s" % (start, end))
        return results
print Solution().summaryRanges([0, 9])
