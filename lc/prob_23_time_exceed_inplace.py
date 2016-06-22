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
        for idx, x in enumerate(list(lists)):
            if not x:
                lists.pop(idx)
        if not lists: return None
        ptrs = lists
        min_val = float('inf')
        for x in xrange(len(lists)):
            if lists[x].val < min_val:
                min_idx = x
                min_val =  lists[x].val
        root = lists[min_idx]
        while(1):
            if not any(ptrs):
                return root
            second_min_val = float('inf')
            second_min_node = None
            second_min_idx = None
            for idx in xrange(len(lists)):
                if ptrs[idx]:
                    if min_idx == idx:
                        if not ptrs[idx].next:
                            continue
                        if ptrs[idx].next.val < second_min_val:
                            second_min_val = ptrs[idx].next.val
                            second_min_node = ptrs[idx].next
                            second_min_idx = idx
                    else:
                        if ptrs[idx].val < second_min_val:
                            second_min_val = ptrs[idx].val
                            second_min_node = ptrs[idx]
                            second_min_idx = idx
            tmp = ptrs[min_idx].next
            ptrs[min_idx].next = second_min_node
            ptrs[min_idx] = tmp
            min_idx = second_min_idx
        return root

a1 = ListNode(1)
a1.next = ListNode(4)
a2 = ListNode(2)
a3 = ListNode(3)

Solution().mergeKLists([None, None])