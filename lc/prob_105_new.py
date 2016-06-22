# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {integer[]} preorder
    # @param {integer[]} inorder
    # @return {TreeNode}
    def buildTree(self, preorder, inorder):
        self.preorder = preorder
        self.inorder = inorder
        return self.recurs(0, 0, len(preorder))

    def recurs(self, preorder_start, inorder_start, length):
        if length >= 1:
            node_val = self.preorder[preorder_start]
            node = TreeNode(node_val)
            node_val_in_inorder_pos = self.inorder[inorder_start:inorder_start + length + 1].index(node_val)
            left_length = node_val_in_inorder_pos
            right_length = length - left_length - 1
            node.left = self.recurs(preorder_start + 1, inorder_start, left_length)
            node.right = self.recurs(preorder_start + left_length + 1, inorder_start + left_length + 1, right_length)
            return node
        return None