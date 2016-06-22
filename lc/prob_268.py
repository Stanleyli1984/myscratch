class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.append(-1)
        for i in xrange(len(nums)):
            while nums[i] != i and nums[i] != -1:
                tmp = nums[i]
                nums[i], nums[tmp] = nums[tmp], nums[i]
        return nums.index(-1)

print Solution().missingNumber([3,1,0])