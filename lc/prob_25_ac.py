class Solution:
    # @param {ListNode} head
    # @param {integer} k
    # @return {ListNode}
    def reverseKGroup(self, head, k):
        if not head:
            return None
        ptr = head
        length = 0
        while ptr:
            ptr = ptr.next
            length += 1
        def get_n_node_after(node, n):
            ptr = node
            for _ in xrange(n):
                ptr = ptr.next
            return ptr
        new_head = None
        ptr = head
        for loop in xrange(length / k):
            for loop_in in xrange(k):
                tmp_next = ptr.next
                if loop_in == 0:
                    if loop == length/k - 1: # last loop
                        ptr.next = get_n_node_after(ptr, k)
                    else:
                        ptr.next = get_n_node_after(ptr, 2 * k - 1)
                else:
                    ptr.next = prev_ptr
                if loop == 0 and loop_in == k - 1:
                    new_head = ptr
                prev_ptr = ptr
                ptr = tmp_next

        if new_head:
            return new_head
        else:
            return head
