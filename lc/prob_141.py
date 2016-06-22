# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        if not head:
            return False
        slow_ptr = fast_ptr = head
        while 1:
            for _ in xrange(2):
                if fast_ptr:
                    fast_ptr = fast_ptr.next
                else:
                    return False
            slow_ptr = slow_ptr.next
            if fast_ptr == slow_ptr:
                return True