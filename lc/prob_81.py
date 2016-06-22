class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {boolean}
    def search(self, nums, target):

        possible_ranges = [(0, len(nums) - 1)]
        while possible_ranges:
            new_ranges = []
            for start, end in possible_ranges:
                mid = (start + end) / 2
                if [1 for x in (mid, start, end) if nums[x] == target]:
                    return True
                if start == end - 1 or start == end:
                    continue
                if nums[start] > nums[mid]:
                    if target > nums[start] or target < nums[mid]:
                        new_ranges.append((start, mid))
                    elif nums[mid] < target < nums[end]:
                        new_ranges.append((mid, end))
                elif nums[mid] > nums[end]:
                    if target > nums[mid] or target < nums[end]:
                        new_ranges.append((mid, end))
                    elif nums[start] < target < nums[mid]:
                        new_ranges.append((start, mid))
                elif nums[start] == nums[mid] < nums[end]:
                    if nums[mid] < target < nums[end]:
                        new_ranges.append((mid, end))
                elif nums[start] < nums[mid] == nums[end]:
                    if nums[start] < target < nums[mid]:
                        new_ranges.append((start, mid))
                elif nums[start] < nums[mid] < nums[end]:
                    if nums[start] < target < nums[mid]:
                        new_ranges.append((start, mid))
                    if nums[mid] < target < nums[end]:
                        new_ranges.append((mid, end))
                else:
                    new_ranges.append((start, mid))
                    new_ranges.append((mid, end))
            possible_ranges = new_ranges
        return False

print Solution().search([3,1,2,2,3], 2)