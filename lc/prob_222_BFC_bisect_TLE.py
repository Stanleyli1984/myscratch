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
        node_count = 0
        level = 0
        level_nodes = [root]
        if not root:
            return 0
        while level_nodes[-1].right:
            node_count += pow(2, level)
            new_level_nodes = []
            for node in level_nodes:
                new_level_nodes.append(node.left)
                new_level_nodes.append(node.right)
            level_nodes = new_level_nodes
            level += 1
        node_count += pow(2, level)
        start = 0
        end = len(level_nodes) - 1
        while True:
            if start == end:
                node_count += start * 2 + (1 if level_nodes[start].left else 0) + (1 if level_nodes[start].right else 0)
                break
            elif start == end - 1:
                node_count += start * 2 + (1 if level_nodes[start].left else 0) + (1 if level_nodes[start].right else 0) +\
                    (1 if level_nodes[end].left else 0) + (1 if level_nodes[end].right else 0)
                break
            mid = (start + end) / 2
            if level_nodes[mid].right:
                start = mid
            else:
                end = mid
        return node_count