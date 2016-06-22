# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} m
    # @param {integer} n
    # @return {ListNode}
    def reverseBetween(self, head, m, n):
        dummy = ListNode(0)
        dummy.next = head
        start = dummy
        for _ in xrange(m - 1):
            start = start.next
        prev = start
        ptr = start.next
        first = ptr
        for _ in xrange(n - m + 1):
            next = ptr.next
            ptr.next = prev
            prev = ptr
            ptr = next
        start.next = prev
        first.next = ptr
        return dummy.next
