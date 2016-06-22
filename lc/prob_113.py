#Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean

    def pathSum(self, root, sum):
        if not root:
            return []
        self.sum = sum
        self.allpaths = []
        self.currentpath = []
        self.traverseTree(root, 0)
        return self.allpaths

    def traverseTree(self, root, current_sum):
        if not root:
            return
        current_sum += root.val
        self.currentpath.append(root.val)
        if not root.left and not root.right:
            if current_sum == self.sum:
                self.allpaths.append(self.currentpath[:])
        self.traverseTree(root.left, current_sum)
        self.traverseTree(root.right, current_sum)
        self.currentpath.pop()


a = TreeNode(1)
#a.left = TreeNode(2)
Solution().pathSum(a, 1)