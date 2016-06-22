#Definition for a  binary tree node
#class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

LEFT = 0
RIGHT = 1

class Solution:
    # @param preorder, a list of integers
    # @param inorder, a list of integers
    # @return a tree node
    def buildTree(self, preorder, inorder):
        if not preorder:
            return None
        root_val = preorder[0]
        position = inorder.index(root_val)
        root = TreeNode(root_val)
        #root.left = self.buildTree(preorder[1:position + 1], inorder[0:position])
        #root.right = self.buildTree(preorder[position + 1:], inorder[position + 1:])
        root.left = self.buildTree(preorder, inorder, position, LEFT)
        root.right = self.buildTree(preorder, inorder, position, RIGHT)
        return root

