# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def sortList(self, head):
        step = 1
        new_head = head
        prev = None
        length = 0
        ptr = head
        if not head:
            return
        while ptr:
            ptr = ptr.next
            length += 1
        while step < length:
            remaining_len = length
            prev = None
            while(1):
                if remaining_len <= step:
                    break
                elif remaining_len <= step * 2:
                    p2_total_step = remaining_len - step
                else:
                    p2_total_step = step
                p1 = new_head if not prev else prev.next
                p2 = p1
                p1_step = p2_step = 0
                for _ in xrange(step):
                    p2 = p2.next
                    if not p2:
                        break
                while not (p1_step == step and p2_step == p2_total_step):
                    if p2_step == p2_total_step:
                        pick = p1
                        pick_n = 1
                    elif p1_step == step:
                        pick = p2
                        pick_n = 2
                    elif p2.val > p1.val:
                        pick = p1
                        pick_n = 1
                    else:
                        pick_n = 2
                        pick = p2
                    if prev:
                        prev.next = pick
                    else:
                        new_head = pick
                    prev = pick
                    if pick_n == 1:
                        p1_step += 1
                        p1 = p1.next
                    else:
                        p2_step += 1
                        last_p2_next = p2.next
                        p2 = p2.next
                prev.next = last_p2_next
                remaining_len -= step * 2
            step *= 2
        return new_head


p1 = ListNode(1)
p2 = ListNode(2)
p3 = ListNode(3)
p4 = ListNode(4)
#p5 = ListNode(5)


p1.next = p2
p2.next = p3
p3.next = p4
#p4.next = p5

Solution().sortList(p1)