# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @return a list of tree node
    def generateTrees(self, n):
        return self.genTrees(1, n + 1)

    def genTrees(self, x, y):
        roots = []
        if x == y: return [None]
        for root_val in xrange (x, y):
            for left in self.genTrees(x, root_val):
                for right in self.genTrees(root_val + 1, y):
                    root = TreeNode(root_val)
                    root.left = left
                    root.right = right
                    roots.append(root)
        return roots