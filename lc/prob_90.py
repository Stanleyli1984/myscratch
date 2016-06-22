import cProfile

class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}

    def __init__(self):
        self.results = set()

    def recurs(self, nums, used, current_idx):
        if current_idx == len(nums):
            return
        for idx in xrange(current_idx, len(nums)):
            tmp = used + [nums[idx]]
            self.results.add(tuple(tmp))
            self.recurs(nums, tmp, idx + 1)

    def subsetsWithDup(self, nums):
        tmp = sorted(nums)
        self.recurs(tmp, [], 0)
        return [[]] + [list(x) for x in self.results]

cProfile.run('print Solution().subsetsWithDup([1,2,3,4,5,6,7,8,10,0])')