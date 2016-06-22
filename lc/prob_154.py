class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def findMin(self, nums):
        if not nums:
            return None
        #if len(set(nums)) == 1:
        #    return nums[0]
        start = 0
        end = len(nums) - 1
        possible_ranges = [(start, end)]
        while possible_ranges:
            new_range = []
            for start, end in possible_ranges:
                mid = (start + end) / 2
                if start == end - 1:
                    if nums[start] > nums[end]:
                        return nums[end]
                    else:
                        continue
                if start == end:
                    continue
                if nums[start] > nums[mid]:
                    new_range.append((start,mid))
                elif nums[mid] > nums[end]:
                    new_range.append((mid, end))
                elif nums[end] > nums[start]:
                    return nums[start]
                else:
                    new_range.append((start, mid))
                    new_range.append((mid, end))
            possible_ranges = new_range
        return nums[0]
print Solution().findMin([3,3,3,3, 3])