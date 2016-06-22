# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode[]} lists
    # @return {ListNode}
    def mergeKLists(self, lists):
        prev = None
        ptrs = set([x for x in lists if x])
        new_head = None
        while ptrs:
            min_v = float('inf')
            for ptr in ptrs:
                if ptr.val < min_v:
                    min_ptr = ptr
                    min_v = ptr.val
            if not prev:
                new_head = min_ptr
            else:
                prev.next = min_ptr
            prev = min_ptr
            if min_ptr.next:
                ptrs.add(min_ptr.next)
            ptrs.remove(min_ptr)
        return new_head

p1 = ListNode(1)
p2 = ListNode(2)
p3 = ListNode(3)
p4 = ListNode(4)
p5 = ListNode(4)
p6 = ListNode(0)
p7 = ListNode(2)



#p5 = ListNode(5)


p1.next = p2
p2.next = p3
p3.next = p4

Solution().mergeKLists([p1, p5, p6, p7])
#p4.next = p5