class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def removeDuplicates(self, nums):
        idx = 0
        while idx < len(nums):
            idx1 = idx+1
            while idx1 < len(nums):
                if nums[idx1] == nums[idx]:
                    nums[idx1] = None
                    idx1 += 1
                else:
                    break
            idx = idx1

        idx_w = 0
        for idx in xrange(0, len(nums)):
            if nums[idx] is not None:
                nums[idx_w] = nums[idx]
                idx_w += 1

        return idx_w
l = [2,2,2,3]
Solution().removeDuplicates(l)
print l