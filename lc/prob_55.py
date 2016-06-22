class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def canJump(self, nums):
        can_reach = 0
        for idx, num in enumerate(nums):
            can_reach = max(can_reach, idx + num)
            if can_reach >= len(nums) - 1:
                return True
            if can_reach < idx + 1:
                return False

print Solution().canJump([3,2,1,0])