# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root:
            return None
        self.recr(root)

    def recr(self, head):
        new_head = None
        ptr = head
        prev = None
        while(ptr):
            if ptr.left and ptr.right:
                ptr.left.next = ptr.right
                if prev:
                    prev.next = ptr.left
                prev = ptr.right
                if not new_head:
                    new_head = ptr.left
            elif ptr.left:
                if prev:
                    prev.next = ptr.left
                prev = ptr.left
                if not new_head:
                    new_head = ptr.left
            elif ptr.right:
                if prev:
                    prev.next = ptr.right
                prev = ptr.right
                if not new_head:
                    new_head = ptr.right
            ptr = ptr.next
        if new_head:
            self.recr(new_head)