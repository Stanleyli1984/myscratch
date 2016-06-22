# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    min_depth = 0xffffffff
    def update_depth(self, depth):
        self.min_depth = depth if depth < self.min_depth else self.min_depth

    def minDepth(self, root):
        if not root:
            return 0
        else:
            self.traverse_tree(root, 1)
        return self.min_depth

    def traverse_tree(self, root, depth):
        if not root:
            return
        elif (not root.left) and (not root.right):
            self.update_depth(depth)
            return
        else:
            self.traverse_tree(root.left, depth + 1)
            self.traverse_tree(root.right, depth + 1)
