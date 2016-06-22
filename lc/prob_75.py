class Solution:
    # @param {integer[]} nums
    # @return {void} Do not return anything, modify nums in-place instead.
     def sortColors(self, nums):
        if not nums:
            return
        p_1 = p = 0
        p_3 = len(nums) - 1
        while p <= p_3:
            print p, p_1, p_3, nums
            if nums[p] == 0:
                nums[p], nums[p_1] = nums[p_1], nums[p]
                p_1 += 1
                p += 1
                continue
            if nums[p] == 2:
                nums[p], nums[p_3] = nums[p_3], nums[p]
                p_3 -= 1
                continue
            if nums[p] == 1:
                p += 1

Solution().sortColors([0,1,1,2,0,0,1,2,1,2])