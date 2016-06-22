class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def permute(self, nums):
        self.nums = nums
        self.length = len(self.nums)
        self.results = []
        if not self.nums:
            return []
        self.recurs(nums, [], self.length)
        return self.results

    def recurs(self, cur, current_l, remaining):
        if remaining == 1:
            for num in cur:
                self.results.append(current_l + [num])
        else:
            for idx, num in enumerate(cur):
                self.recurs(cur[:idx] + cur[idx+1:], current_l + [cur[idx]], remaining - 1)


print Solution().permute([1,2,3])