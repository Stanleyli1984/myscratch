# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def countNodes(self, root):
        def count_node(level):
            total = 0
            for i in xrange(level):
                total += pow(2, i)
            return total
        if not root:
            return 0
        node = root
        l_level = 0
        while node:
            node = node.left
            l_level += 1
        r_level = 0
        node = root
        while node:
            node = node.right
            r_level += 1
        if l_level == r_level:
            return count_node(l_level)
        self.total = count_node(r_level)
        self.recr(root, l_level - 1)
        return self.total

    def recr(self, node, l_num):
        l_node = node.left
        r_node = node.right
        l_level = 0
        while l_node:
            l_node = l_node.right
            l_level += 1
        r_level = 0
        while r_node:
            r_node = r_node.left
            r_level += 1
        if r_level == l_level - 1:
            self.total += pow(2, l_num - 1)
            return
        else:
            if l_level == l_num:
                self.total += pow(2, l_num - 1)
                self.recr(node.right, l_num-1)
            else:
                self.recr(node.left, l_num-1)