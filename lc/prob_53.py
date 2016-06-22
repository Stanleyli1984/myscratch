class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def maxSubArray(self, nums):
        prev_sum = 0
        sums = []
        for num in nums:
            if prev_sum < 0:
                new_sum = num
            else:
                new_sum = num + prev_sum
            sums.append(new_sum)
            prev_sum = new_sum
        print sums
        return max(sums)

a = [-2, 1, -3, 4, -1, 2 ,1, -5, 4]
print Solution().maxSubArray(a)

''' check divid-and-conque solution'''