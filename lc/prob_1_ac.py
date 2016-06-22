class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def twoSum(self, nums, target):
        h = {}
        for idx, num in enumerate(nums):
            if num not in h:
                h[target - num] = idx
            else:
                return sorted([idx + 1, h[target - num] + 1])