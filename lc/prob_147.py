# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def insertionSortList(self, head):
        if not head:
            return None
        dummy_head = ListNode(float('-inf'))
        dummy_head.next = head
        o_ptr = head
        prev = dummy_head
        while o_ptr:
            i_ptr = dummy_head
            next_o = o_ptr.next
            moved = False
            if o_ptr.val < prev.val:
                while i_ptr.next != o_ptr:
                    if i_ptr.next.val >= o_ptr.val:
                        prev.next = o_ptr.next
                        o_ptr.next = i_ptr.next
                        i_ptr.next = o_ptr
                        moved = True
                        break
                    i_ptr = i_ptr.next
            if not moved:
                prev = o_ptr
            o_ptr = next_o
        return dummy_head.next

p1 = ListNode(1)
p2 = ListNode(2)
p3 = ListNode(3)
p4 = ListNode(4)
p5 = ListNode(5)


p1.next = p2
p2.next = p3
p3.next = p4
p4.next = p5

Solution().insertionSortList(p1)