# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


#extra memory
class Solution_1:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        ptr = head
        prev_val = None
        new_ptr = new_head = None
        while (ptr):
            if (ptr.val!=prev_val and (not ptr.next or ptr.val != ptr.next.val)):
                if (new_ptr):
                    new_ptr.next = ListNode(ptr.val)
                    new_ptr = new_ptr.next
                else:
                    new_ptr= ListNode(ptr.val)
                    new_head = new_ptr
            prev_val = ptr.val
            ptr = ptr.next
        return new_head

#in-place
class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        ptr = head
        prev_val = None
        q_ptr = new_head = None
        while (ptr):
            if (ptr.val!=prev_val and (not ptr.next or ptr.val != ptr.next.val)):
                if (not new_head):
                    new_head = q_ptr = ptr
                else:
                    q_ptr.next = ptr
                    q_ptr = ptr
            prev_val = ptr.val
            ptr = ptr.next
        if q_ptr:
            q_ptr.next = None
        return new_head



