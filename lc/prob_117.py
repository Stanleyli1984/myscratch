# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        if not root or not root.left or not root.right:
            return
        else:
            self.populate(root.left, root.right)

    def populate(self, left, right):
        left.next = right
        if left.left:
            self.populate(left.left, left.right)
            self.populate(left.right, right.left)
            self.populate(right.left, right.right)