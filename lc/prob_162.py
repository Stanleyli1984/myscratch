class Solution:
    # @param nums, an integer[]
    # @return an integer
    def findPeakElement(self, nums):
        if len(nums) == 1:
            return 0
        if nums[0] > nums[1]:
            return 0
        if nums[-1] > nums[-2]:
            return len((nums)) - 1
        l = 0
        r = len(nums) - 1
        while True:
            #print r, l, (r + l) / 2
            if r - l == 2:
                return (r + l) / 2
            if r - l == 3:
                return (r + l) / 2 if nums[(r + l) / 2] > nums[(r + l) / 2 + 1] else (r + l) / 2 + 1
            m = (r + l) /2
            if nums[m - 1] < nums[m] > nums[m + 1]:
                return m
            if nums[m - 1] > nums[m]:
                r = m
            elif nums[m] < nums[m + 1]:
                l = m

print Solution().findPeakElement([1,2,3,7,10,1, 3,2])