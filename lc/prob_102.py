# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrder(self, root):
        all_vals = []
        if not root:
            return all_vals
        level_nodes = [root]
        while True:
            level_vals = [x.val for x in level_nodes]
            if not level_nodes:
                break
            else:
                all_vals.append(level_vals)
            level_nodes_next = []
            for x in level_nodes:
                if x.left:
                    level_nodes_next.append(x.left)
                if x.right:
                    level_nodes_next.append(x.right)
            level_nodes = level_nodes_next
        return all_vals

a = TreeNode(1)
a.left = TreeNode(2)

b = Solution()
print b.levelOrder(a)
