class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def maxProduct(self, nums):
        max_list = [nums[0]]
        min_list = [nums[0]]
        for i in xrange(1, len(nums)):
            #print max_list, min_list
            max_tmp = max(max_list[-1] * nums[i], min_list[-1] * nums[i], nums[i])
            min_list.append(min(max_list[-1] * nums[i], min_list[-1] * nums[i], nums[i]))
            max_list.append(max_tmp)
        #print max_list, min_list
        return max(max_list + min_list)

print Solution().maxProduct([-4, -3, -2])