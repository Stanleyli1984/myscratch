# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    sum = 0

    def __init__(self):
        self.sum = 0

    def sumNumbers(self, root):
        if not root:
            return 0
        self.traverseTree(root, 0)
        return self.sum

    def traverseTree(self, root, branch_value):
        if not root.left and not root.right:
            self.sum += branch_value * 10 + root.val
        else:
            if root.left:
                self.traverseTree(root.left, branch_value * 10 + root.val)
            if root.right:
                self.traverseTree(root.right, branch_value * 10 + root.val)
