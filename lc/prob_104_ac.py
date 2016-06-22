#Definition for a  binary tree node

#class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    max_depth = 0
    current_depth = 0
    def maxDepth(self, root):
        if not root:
            return 0
        self.current_depth += 1
        if self.current_depth > self.max_depth:
            self.max_depth = self.current_depth
        if root.left:
            self.maxDepth(root.left)
        if root.right:
            self.maxDepth(root.right)

        self.current_depth -= 1
        return self.max_depth

