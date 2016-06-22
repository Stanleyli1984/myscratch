# Definition for singly-linked list.
#class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:

    def find_kth_node(self, head, k): #k : 0 to len-1
        ptr = head
        for _ in xrange(k):
            ptr = ptr.next
        return ptr

    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def rotateRight(self, head, k):
        if (not head):
            return None
        len = 1
        ptr = head
        while (ptr.next):
            ptr = ptr.next
            len += 1
        ptr.next = head
        new_tail = self.find_kth_node(head, -(k+1) % len)
        new_head = new_tail.next
        new_tail.next = None
        return new_head
