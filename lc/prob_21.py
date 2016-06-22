# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param two ListNodes
    # @return a ListNode
    def mergeTwoLists(self, l1, l2):
        in_middle = lambda x, y, z: (y <= x <= z) or (z <= x <= y)
        l1_ptr = l1
        l2_ptr = l2
        if (not l1):
            return l2
        while(l2_ptr):
            if (not l1_ptr.next or in_middle(l2_ptr.val, l1_ptr.val, l1_ptr.next.val)):
                tmp = ListNode(l2_ptr.val)
                tmp.next = l1_ptr.next
                l1_ptr.next = tmp
                l1_ptr = tmp
            l2_ptr = l2_ptr.next
        return l1