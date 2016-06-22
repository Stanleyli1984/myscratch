# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {integer[]} nums
    # @return {TreeNode}
    def sortedArrayToBST(self, nums):
        if not nums:
            return None
        self.nums = nums
        return self.recur(0, len(nums) - 1)

    def recur(self, start, end):
        if end < start:
            return None
        mid = (start + end) / 2
        node = TreeNode(self.nums[mid])
        node.left = self.recur(start, mid - 1)
        node.right = self.recur(mid + 1, end)
        return node