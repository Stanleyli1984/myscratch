class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def rob(self, nums):
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        results = []
        for l in ([0] + nums[1:], nums[:-1] + [0]):
            dp_array = [l[0], max(l[0], l[1])]
            for i in xrange(2, len(l)):
                dp_array.append(max(dp_array[i-1], dp_array[i - 2] + l[i]))
            results.append(dp_array[-1])
        return max(results)

print Solution().rob([100,1,1,1,100])