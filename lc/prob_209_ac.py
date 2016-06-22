class Solution:
    # @param {integer} s
    # @param {integer[]} nums
    # @return {integer}
    def minSubArrayLen(self, s, nums):
        mlen = float('inf')
        if not nums:
            return 0
        p1 = p2 = nsum = 0
        while True:
            if nsum < s:
                nsum += nums[p2]
            while nsum >= s:
                if p2 - p1 + 1 < mlen:
                    mlen = p2 - p1 + 1
                if p1 < p2:
                    nsum -= nums[p1]
                    p1 += 1
                else:
                    break
            if p2 == len(nums) - 1:
                if p1 == 0 and nsum < s:
                    return 0
                return mlen
            p2 += 1

print Solution().minSubArrayLen(7, [1,2,3,9,1,1])