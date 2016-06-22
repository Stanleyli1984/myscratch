# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[]}
    def rightSideView(self, root):
        def get_all_leaf_nodes(roots):
            tmp = []
            for root in roots:
                if root.left:
                    tmp.append(root.left)
                if root.right:
                    tmp.append(root.right)
            return tmp

        if not root:
            return []
        results = []
        leaf_nodes = [root]
        while leaf_nodes:
            results.append(leaf_nodes[-1].val)
            leaf_nodes = get_all_leaf_nodes(leaf_nodes)

        return results


