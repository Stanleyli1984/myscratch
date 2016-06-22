# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} x
    # @return {ListNode}
    def partition(self, head, x):
        dummy_heads = (ListNode(-1), ListNode(-1))
        ptrs = [dummy_heads[0],  dummy_heads[1]]
        ptr = head
        while ptr:
            if ptr.val < x:
                ptrs[0].next = ptr
                ptr = ptr.next
                ptrs[0] = ptrs[0].next
            else:
                ptrs[1].next = ptr
                ptr = ptr.next
                ptrs[1] = ptrs[1].next
        ptrs[0].next = dummy_heads[1].next
        ptrs[1].next = None
        return dummy_heads[0].next

a = ListNode(2)
b = ListNode(1)
a.next = b

Solution().partition(a, 2)