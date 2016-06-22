# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {void} Do not return anything, modify head in-place instead.
    def reorderList(self, head):
        ptr = head
        if not ptr:
            return None
        node_array = []
        while ptr:
            node_array.append(ptr)
            ptr = ptr.next
        array_ptr1 = 0
        array_ptr2 = len(node_array) - 1
        while array_ptr1 < array_ptr2:
            node_array[array_ptr1].next = node_array[array_ptr2]
            array_ptr1 += 1
            if array_ptr1 < array_ptr2:
                node_array[array_ptr2].next = node_array[array_ptr1]
                array_ptr2 -= 1
        node_array[array_ptr1].next = None
        #return node_array[0]