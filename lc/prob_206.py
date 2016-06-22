# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def reverseList(self, head):
        if not head:
            return None
        prev = None
        ptr = head
        while ptr:
            next = ptr.next
            ptr.next = prev
            prev = ptr
            ptr = next
        return prev