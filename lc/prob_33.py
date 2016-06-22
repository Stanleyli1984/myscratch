class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def search(self, nums, target):
        prange = (0, len(nums) - 1)
        if not nums:
            return -1
        while prange:
            new_ranges = None
            mid_idx = (prange[0] + prange[1])/2
            mid = nums[mid_idx]
            for crange in ((prange[0], mid_idx), (mid_idx, prange[1])):
                for n in xrange(2):
                    if nums[crange[n]] == target:
                        return crange[n]
                if prange[0] <= prange[1] - 2:
                    if nums[crange[0]] < target < nums[crange[1]]:
                        new_ranges = crange
                        break
                    if (nums[crange[0]] > nums[crange[1]]) and (target > nums[crange[0]] or target < nums[crange[1]]):
                        new_ranges = crange
                        break
            prange = new_ranges
        return -1

print Solution().search([4,5,6,7,8,1,2,3], 8)