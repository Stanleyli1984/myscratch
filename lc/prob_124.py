# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def maxPathSum(self, root):
        self.max = float('-inf')
        if not root:
            return None
        self.recr(root)
        return self.max

    def recr(self, node):
        Lmax = 0 if not node.left else self.recr(node.left)
        Rmax = 0 if not node.right else self.recr(node.right)
        if Lmax > Rmax:
            child_max = Lmax
        else:
            child_max = Rmax
        max_node = max(Lmax + node.val + Rmax, child_max + node.val, node.val)
        if max_node > self.max:
            self.max = max_node
        return max(child_max+node.val, node.val)