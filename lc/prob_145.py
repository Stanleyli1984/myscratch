UPLEFT = 0
UPRIGHT = 1
DOWN = 2

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def postorderTraversal(self, root):
        vals = []
        node_stack = []
        current = root
        direction = DOWN
        if not root:
            return []
        while True:
            if direction == DOWN:
                if current.left:
                    node_stack.append(current)
                    current = current.left
                elif current.right:
                    node_stack.append(current)
                    current = current.right
                else:
                    vals.append(current.val)
                    if current == root:
                        break
                    direction = UPLEFT if current == node_stack[-1].left else UPRIGHT
                    current = node_stack.pop()
            elif direction == UPLEFT:
                if current.right:
                    node_stack.append(current)
                    current = current.right
                    direction = DOWN
                else:
                    vals.append(current.val)
                    if current == root:
                        break
                    direction = UPLEFT if current == node_stack[-1].left else UPRIGHT
                    current = node_stack.pop()
            elif direction == UPRIGHT:
                vals.append(current.val)
                if current == root:
                    break
                direction = UPLEFT if current == node_stack[-1].left else UPRIGHT
                current = node_stack.pop()
        return vals

# # Definition for a  binary tree node
class TreeNode:
     def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
#
# class Solution:
#     # @param root, a tree node
#     # @return a list of integers
#     def postorderTraversal(self, root):
#         node_stack = []
#         current = root
#         vals = []
#         tmp_nodes = []
#         while(node_stack or current):
#             if not current:
#                 current = node_stack.pop()
#                 tmp_nodes.append(current)
#                 if (is_left):
#                     pass
#                 else:
#                     for tmp_node in reversed(tmp_nodes):
#                         if current == tmp_node:
#                             break
#                         else:
#                             vals.append(tmp_node.val)
#                             tmp_nodes.pop()
#                 is_left = False
#                 current = current.right
#             else:
#                 node_stack.append(current)
#                 current = current.left
#                 is_left = True
#         return vals + [x.val for x in reversed(tmp_nodes)]
#
a = TreeNode(2)
a.left = TreeNode(3)
a.left.left = TreeNode(1)
print Solution().postorderTraversal(a)