class Solution:
    # @param {integer[]} nums
    # @return {void} Do not return anything, modify nums in-place instead.
    def nextPermutation(self, nums):
        if len(nums) == 1:
            return
        if len(nums) == 2:
            nums[0], nums[1] = nums[1], nums[0]
            return
        for i in xrange(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                for j in xrange(len(nums) - 1, i, -1):
                    if nums[j] > nums[i]:
                        nums[i], nums[j] = nums[j], nums[i]
                        nums[i+1:] = sorted(nums[i+1:])
                        return
        else:
            nums.sort()

print Solution().nextPermutation([1,2,3])