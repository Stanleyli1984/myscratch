class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def permuteUnique(self, nums):
        self.nums = nums
        self.length = len(self.nums)
        self.results = []
        if not self.nums:
            return []
        self.recurs(nums, [], self.length)
        return self.results

    def recurs(self, cur, current_l, remaining):
        visited = set()
        if remaining == 1:
            for num in cur:
                if num not in visited:
                    self.results.append(current_l + [num])
                    visited.add(num)
        else:
            for idx, num in enumerate(cur):
                if num not in visited:
                    self.recurs(cur[:idx] + cur[idx+1:], current_l + [cur[idx]], remaining - 1)
                    visited.add(num)

print Solution().permuteUnique([1,1,2])