# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def swapPairs(self, head):
        dummy_head = ListNode(-1)
        dummy_head.next = head
        prev = dummy_head
        node = head
        while node and node.next:
            tmp = node.next.next
            node.next.next = node
            prev.next = node.next
            node.next = tmp
            prev = node
            node = tmp
        return dummy_head.next