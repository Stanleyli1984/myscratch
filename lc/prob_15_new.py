class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def threeSum(self, nums):
        table = {}
        results = set()
        for idx, num in enumerate(nums):
            if num < 0:
                table[-num] = idx
        for i in xrange(0, len(nums)):
            for j in xrange(i+1, len(nums)):
                if nums[i]+nums[j] in table and table[nums[i]+nums[j]] not in [i, j]:
                    results.add(tuple(sorted([nums[i], nums[j], -nums[i]-nums[j]])))
        if len([1 for x in nums if x==0]) >= 3:
            results.add((0,0,0))
        return list(results)


print Solution().threeSum([-1,0,1,2,-1,-4])
