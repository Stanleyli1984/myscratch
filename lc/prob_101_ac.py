# Definition for a  binary tree node
#class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

LEFT_FIRST = 0
RIGHT_FIRST = 1

class Solution:
    # @param root, a tree node
    # @return a boolean

    def isSymmetric(self, root):
        #print list(self.traverse_tree(root, LEFT_FIRST))
        #print list(self.traverse_tree(root, RIGHT_FIRST))
        return list(self.traverse_tree(root, LEFT_FIRST)) == list(self.traverse_tree(root, RIGHT_FIRST))

    def traverse_tree(self, root, direction):
        if not root:
            yield None
            return
        else:
            yield root.val
        if direction == LEFT_FIRST:
            # A wierd method in Python 2. Python 3 can use "yield from"
            # http://stackoverflow.com/questions/248830/python-using-a-recursive-algorithm-as-a-generator
            for x in self.traverse_tree(root.left, direction):
                yield x
            for x in self.traverse_tree(root.right, direction):
                yield x
        if direction == RIGHT_FIRST:
            for x in self.traverse_tree(root.right, direction):
                yield x
            for x in self.traverse_tree(root.left, direction):
                yield x

