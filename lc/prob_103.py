# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def zigzagLevelOrder(self, root):
        if not root:
            return []
        nodes = [root]
        vals = []
        left2right = True
        while nodes:
            tmp_vals = []
            tmp_nodes = []
            if left2right:
                for node in reversed(nodes):
                    if node.left:
                        tmp_nodes.append(node.left)
                    if node.right:
                        tmp_nodes.append(node.right)
                    tmp_vals.append(node.val)
            else:
                for node in reversed(nodes):
                    if node.right:
                        tmp_nodes.append(node.right)
                    if node.left:
                        tmp_nodes.append(node.left)
                    tmp_vals.append(node.val)
            nodes = tmp_nodes
            vals.append(tmp_vals)
            left2right = not left2right
        return vals