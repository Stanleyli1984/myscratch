# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {void} Do not return anything, modify root in-place instead.
    def recoverTree(self, root):
        self.wrong_nodes = []
        self.prev = None
        self.recur(root)
        if len(self.wrong_nodes) == 1:
            self.wrong_nodes[0][0].val, self.wrong_nodes[0][1].val = self.wrong_nodes[0][1].val, self.wrong_nodes[0][0].val
        if len(self.wrong_nodes) == 2:
            self.wrong_nodes[0][0].val, self.wrong_nodes[1][1].val = self.wrong_nodes[1][1].val, self.wrong_nodes[0][0].val

    def recur(self, node):
        if node:
            self.recur(node.left)
            if self.prev and self.prev.val > node.val:
                self.wrong_nodes.append((self.prev, node))
            self.prev = node
            self.recur(node.right)