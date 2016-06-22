# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return nothing, do it in place
    def flatten(self, root):
        self.traverseTree(root)

    def traverseTree(self, root):
        if not root:
            return None
        leaf_left = self.traverseTree(root.left)
        leaf_right = self.traverseTree(root.right)

        if root.left: # or leaf_left
            leaf_left.right = root.right
            root.right = root.left
            root.left = None

        if leaf_right:
            return leaf_right
        elif leaf_left:
            return leaf_left
        else:
            return root

a = TreeNode(1)
a.left = TreeNode(2)
a.left.left = TreeNode(3)

Solution().flatten(a)
