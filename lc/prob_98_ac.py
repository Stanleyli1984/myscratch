class Solution:
    # @param root, a tree node
    # @return a boolean
    def isValidBST(self, root):
        if not root:
            return True
        left_vals = self.treeTraverse(root.left)
        right_vals = self.treeTraverse(root.right)
        left_ok = not left_vals or max(left_vals) < root.val
        right_ok = not right_vals or min(right_vals) > root.val
        if not (left_ok and right_ok):
            return False
        return self.isValidBST(root.left) and self.isValidBST(root.right)

    def treeTraverse(self, root):
        if not root:
            return []
        vals = []
        vals.extend(self.treeTraverse(root.left))
        vals.extend(self.treeTraverse(root.right))
        vals.append(root.val)
        return vals
