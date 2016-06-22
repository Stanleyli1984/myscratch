import sys

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def firstMissingPositive(self, nums):
        for i in xrange(len(nums)):
            if nums[i] < 0:
                nums[i] = 0

        for i in xrange(len(nums)):
            if nums[i] != 0:
                tmp = nums[i] if nums[i] > 0 else -nums[i]
                if tmp <= len(nums):
                    if nums[tmp-1] > 0:
                        nums[tmp-1] = -nums[tmp-1]
                    elif nums[tmp-1] == 0:
                        nums[tmp-1] = -sys.maxint - 1
        least = 1
        for num in nums:
            if num < 0:
                least += 1
            else:
                return least
        return least

print  Solution().firstMissingPositive([0])