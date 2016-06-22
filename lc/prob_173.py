# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


''' only push left node into stack.
if the node is in stack, mean, current running node is part of its left node tree.
'''

class BSTIterator:
    # @param root, a binary search tree's root node
    def __init__(self, root):
        node = root
        self.stack = []
        while node:
            self.stack.append(node)
            node = node.left

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        return True if self.stack else False

    # @return an integer, the next smallest number
    def next(self):
        c_node = self.stack.pop()
        value = c_node.val
        r_node = c_node.right
        while r_node:
            self.stack.append(r_node)
            r_node = r_node.left
        return value

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())