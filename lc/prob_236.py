# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        self.p = p
        self.q = q
        node, _ = self.recr(root)
        return node

    def recr(self, node):
        if not node:
            return None, None
        found_l, l = self.recr(node.left)
        if found_l:
            return found_l, None
        found_r, r = self.recr(node.right)
        if found_r:
            return found_r, None
        if l and r:
            return node, None
        for child_node in (l, r):
            if child_node:
                if node in (self.p, self.q):
                    return node, None
                else:
                    return None, child_node
        if node in (self.p, self.q):
            return None, node
        return None, None
