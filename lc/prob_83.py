# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        head_ptr = head
        while(head_ptr):
            if (head_ptr.next and (head_ptr.val == head_ptr.next.val)):
                head_ptr.next = head_ptr.next.next
            else:
                head_ptr = head_ptr.next
        return head