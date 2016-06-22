# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def preorderTraversal(self, root):
        stack = []
        current = root
        vals = []
        while(stack or current):
            #current = stack[-1]
            if not current:
                current = stack.pop()
                current = current.right
            else:
                stack.append(current)
                vals.append(current.val)
                current = current.left
        return vals