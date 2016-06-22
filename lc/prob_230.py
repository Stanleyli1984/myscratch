# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @param {integer} k
    # @return {integer}
    def kthSmallest(self, root, k):
        if not root:
            return None
        self.values = {}
        self.recr_c(root)
        self.k = k
        return self.recr_s(root, k)

    def recr_c(self, node):
        if not node:
            return 0
        value = self.recr_c(node.left) + 1
        self.values[node] = value
        return value + self.recr_c(node.right)

    def recr_s(self, node, remaining):
        value = self.values[node]
        if remaining == value:
            return node.val
        elif remaining < value:
            return self.recr_s(node.left, remaining)
        else:
            return self.recr_s(node.right, remaining - value)