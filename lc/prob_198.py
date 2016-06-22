class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def rob(self, nums):
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        dp_array = [nums[0], max(nums[0], nums[1])]
        for i in xrange(2, len(nums)):
            dp_array.append(max(dp_array[i-1], dp_array[i - 2] + nums[i]))
        return dp_array[-1]

print Solution().rob([100,1,1,1,100])