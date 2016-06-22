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
    def buildTree(self, inorder, postorder):
        self.postorder = postorder
        self.inorder = inorder
        return self.recurs(0, 0, len(postorder))

    def recurs(self, inorder_start, postorder_start, length):
        if length >= 1:
            node_val = self.postorder[postorder_start + length - 1]
            node = TreeNode(node_val)
            node_val_in_inorder_pos = self.inorder[inorder_start:inorder_start + length + 1].index(node_val)
            left_length = node_val_in_inorder_pos
            right_length = length - left_length - 1
            node.left = self.recurs(inorder_start, postorder_start, left_length)
            node.right = self.recurs(inorder_start + left_length + 1, postorder_start + left_length, right_length)
            return node
        return None