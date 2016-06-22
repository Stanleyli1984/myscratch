class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def searchInsert(self, nums, target):
        if not nums:
            return 0
        start = 0
        end = len(nums) - 1
        while True:
            if end == start:
                if nums[start] < target:
                    return start + 1
                else:
                    return start
            mid = (start + end) /2
            if target < nums[start]:
                return start
            if target > nums[end]:
                return end + 1
            if nums[mid] < target:
                start = mid + 1
            elif nums[mid] == target:
                return mid
            else:
                if mid - 1 >= start:
                    end = mid - 1

print Solution().searchInsert([1,3], 2)