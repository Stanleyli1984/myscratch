#Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean

    def hasPathSum(self, root, sum):
        if not root:
            return False
        self.found = False
        self.sum = sum
        self.traverseTree(root, 0)
        return self.found

    def traverseTree(self, root, current_sum):
        if not root:
            return
        current_sum += root.val
        if not root.left and not root.right:
            if current_sum == self.sum:
                    self.found = True
            return
        self.traverseTree(root.left, current_sum)
        if not self.found:
            self.traverseTree(root.right, current_sum)


#a = TreeNode(1)
#a.left = TreeNode(2)
#Solution().hasPathSum(a, 1)