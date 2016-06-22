# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {ListNode} head
    # @return {TreeNode}
    def sortedListToBST(self, head):
        ptr = head
        length = 0
        while ptr:
            ptr = ptr.next
            length += 1
        return self.recr(head, length)

    def recr(self, ptr, length):
        if length <= 0:
            return None
        else:
            n_ptr = ptr
            for _ in xrange(length/2):
                n_ptr = n_ptr.next
            node = TreeNode(n_ptr.val)
            node.left = self.recr(ptr, length / 2)
            if length % 2 == 0:
                node.right = self.recr(n_ptr.next, length / 2 - 1)
            else:
                node.right = self.recr(n_ptr.next, (length - 1) / 2)
            return node