class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def searchRange(self, nums, target):
        #mid = len(nums)/2
        start_range = [0, len(nums) - 1]
        end_range = [0, len(nums) - 1]
        result = [None, None]
        if not nums:
            return [-1, -1]
        #for s_range in (start_range, end_range):
        while start_range or end_range:
            if start_range:
                if nums[start_range[1]] < target or nums[start_range[0]] > target:
                    return [-1, -1]
                mid = (start_range[0] + start_range[1]) / 2
                if nums[start_range[0]] == target:
                    result[0] = start_range[0]
                    new_start_range = None
                elif nums[start_range[0]] < target <= nums[mid]:
                    new_start_range = (start_range[0]+1, mid)
                elif nums[mid] < target <= nums[start_range[1]]:
                    new_start_range = (mid + 1, start_range[1])
                #elif target == nums[start_range[1]]:
                #    result[0] = start_range[1]
                #    new_start_range = None
            if end_range:
                if nums[end_range[1]] < target or nums[end_range[0]] > target:
                    return [-1, -1]
                mid = (end_range[0] + end_range[1]) / 2 + 1
                if nums[end_range[1]] == target:
                    result[1] = end_range[1]
                    new_end_range = None
                elif nums[end_range[1]] > target >= nums[mid]:
                    new_end_range = (mid, end_range[1] -1)
                elif nums[mid] > target >= nums[end_range[0]]:
                    new_end_range = (end_range[0], mid-1)
                #elif target == nums[end_range[0]]:
                #    result[1] = end_range[0]
                #    new_end_range = None
            start_range, end_range = new_start_range, new_end_range
        return result

print Solution().searchRange([1,2,2,3,4,4,4], 4)