import math
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        end = len(nums) - 1
        start = 1
        while True:
            cnt1 = cnt2 = cnt3 = 0
            mid = (start + end) / 2.0
            for num in nums:
                if num == mid:
                    cnt3 += 1
                elif start <= num < mid:
                    cnt1 += 1
                elif mid < num <= end:
                    cnt2 += 1

            if cnt3 > 1:
                return int(mid)
            elif cnt1 > cnt2:
                end = math.floor(mid)
            else:
                start = math.ceil(mid)

print Solution().findDuplicate([1,2,2])