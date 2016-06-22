# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def mergeTwoLists(self, l1, l2):
        prev = None
        p1 = l1
        p2 = l2
        if not l1:
            return l2
        elif not l2:
            return l1

        new_head = None
        while p1 and p2:
            if p1.val < p2.val:
                if not prev:
                    new_head = p1
                else:
                    prev.next = p1
                prev = p1
                p1 = p1.next
            else:
                if not prev:
                    new_head = p2
                else:
                    prev.next = p2
                prev = p2
                p2 = p2.next
        if not p1:
            prev.next = p2
        else:
            prev.next = p1
        return new_head

