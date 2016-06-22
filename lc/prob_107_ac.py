#Definition for a  binary tree node
#class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    all_vals = []
    def levelOrderBottom(self, root):
        self.all_vals = []
        self.traverse_tree(root, 0)
        return self.all_vals[::-1]

    def insert_val(self, val, depth):
        if len(self.all_vals) < depth + 1:
            self.all_vals.append([])
        self.all_vals[depth].append(val)

    def traverse_tree(self, root, depth):
        if not root:
            return
        else:
            self.insert_val(root.val, depth)
            self.traverse_tree(root.left, depth + 1)
            self.traverse_tree(root.right, depth + 1)

#a = TreeNode(1)
#a.left = TreeNode(2)
#a.right = TreeNode(3)
#a.left.left = TreeNode(4)
#a.left.right = TreeNode(5)
#b = Solution()
#print b.levelOrderBottom(a)