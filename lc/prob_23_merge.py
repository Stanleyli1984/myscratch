__author__ = 'zhongqil'


class Solution:
    # @param {ListNode[]} lists
    # @return {ListNode}
    def mergeKLists(self, lists):
        lists = [x for x in lists if x]
        if not lists:
            return None
        while (len(lists) > 1):
            new_list = []
            for l in xrange(0, len(lists), 2):
                if l + 1 < len(lists):
                    new_list.append(self.mergeTwoLists(lists[l], lists[l+1]))
                else:
                    new_list.append(lists[l])
            lists = new_list
        return lists[0]

    def mergeTwoLists(self, l1, l2):
        prev = None
        p1 = l1
        p2 = l2
        if not l1:
            return l2
        elif not l2:
            return l1

        new_head = None
        while p1 and p2:
            if p1.val < p2.val:
                if not prev:
                    new_head = p1
                else:
                    prev.next = p1
                prev = p1
                p1 = p1.next
            else:
                if not prev:
                    new_head = p2
                else:
                    prev.next = p2
                prev = p2
                p2 = p2.next
        if not p1:
            prev.next = p2
        else:
            prev.next = p1
        return new_head
