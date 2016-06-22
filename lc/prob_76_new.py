from collections import deque

class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class DoubleList(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def r_push(self, node):
        node.next = self.head
        if self.head:
            self.head.prev = node
        else:
            self.tail = node
        self.head = node
        self.length += 1

    def l_pop(self):
        node = Node(self.tail)
        if self.tail.prev:
            self.tail.prev.next = None
        del self.tail
        self.tail = node.prev
        self.length -= 1
        return node.val

    def peek_left(self):
        return self.tail.val

    def del_node(self, node):
        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next
        if node.next:
            node.next.prev = node.prev
        else:
            self.tail = node.prev
        del node
        self.length -= 1

class Solution:
    # @param {string} s
    # @param {string} t
    # @return {string}
    def minWindow(self, s, t):
        pos_dict = {}
        length_dict = {}
        dlist = DoubleList()
        for char in t:
            length_dict[char] = length_dict.get(char, 0) + 1
        min_length = float('+inf')
        minimal = None
        for idx, char in enumerate(s):
            if char in t:
                if char in pos_dict and len(pos_dict[char]) == length_dict[char]:
                    dlist.del_node(pos_dict[char][0])
                new_node = Node(idx)
                dlist.r_push(new_node)
                if dlist.length > len(t):
                    dlist.l_pop()

                if char not in pos_dict:
                    pos_dict[char] = deque(maxlen=length_dict[char])
                pos_dict[char].append(new_node)

                if dlist.length == len(t):
#                    idxes[idx] = pos_dict[next(iter(pos_dict))]
                    moft_left_element = dlist.peek_left()
                    if idx - moft_left_element < min_length:
                        min_length = idx - moft_left_element
                        minimal = (moft_left_element, idx)
        if minimal:
            return s[minimal[0]: minimal[1]+1]
        else:
            return ""

#print Solution().minWindow("ADOBECODEBANC", "ABC")
print Solution().minWindow("aa", "aa")
