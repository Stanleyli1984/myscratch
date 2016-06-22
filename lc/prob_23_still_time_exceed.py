# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param a list of ListNode
    # @return a ListNode
    def mergeKLists(self, lists):
        if not lists: return None
        while None in lists:
                lists.remove(None)
        if not lists: return None
        ptrs = lists
        root = None
        prev = None
        while (any(ptrs)):
            min_val = float('inf')
            for x in xrange(len(lists)):
                if not ptrs[x]:
                    continue
                if ptrs[x].val < min_val:
                    min_idx = x
                    min_val =  ptrs[x].val
            new_node = ListNode(ptrs[min_idx].val)
            if prev:
                prev.next = new_node
            if not root:
                root = new_node
            prev = new_node
            ptrs[min_idx] = ptrs[min_idx].next

a1 = ListNode(1)
a1.next = ListNode(4)
a2 = ListNode(2)
a3 = ListNode(3)

Solution().mergeKLists([a1, a2,a3])