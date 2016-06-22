# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {boolean}
    def isBalanced(self, root):
        if not root:
            return True
        is_balanced, _ = self.recur(0, root)
        return is_balanced

    def recur(self, height, node):
        if not node:
            return True, height
        l_balanced, l_height = self.recur(height + 1, node.left)
        if not l_balanced:
            return False, -1
        r_balanced, r_height = self.recur(height + 1, node.right)
        if not r_balanced:
            return False, -1
        if abs(l_height - r_height) <= 1:
            return True, max(l_height, r_height)
        else:
            return False, -1