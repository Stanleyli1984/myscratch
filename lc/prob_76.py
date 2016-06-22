from collections import OrderedDict, deque

class Solution:
    # @param {string} s
    # @param {string} t
    # @return {string}
    def minWindow(self, s, t):
        pos_dict = OrderedDict()
        length_dict = {}
        for char in t:
            length_dict[char] = length_dict.get(char, 0) + 1
        min_length = float('+inf')
        minimal = None
        total_len = 0
        for idx, char in enumerate(s):
            if char in t:
                old_len = 0
                if char in pos_dict:
                    v = pos_dict[char]
                    old_len = len(v)
                    del pos_dict[char]
                    pos_dict[char] = v
                else:
                    pos_dict[char] = deque(maxlen=length_dict[char])
                pos_dict[char].append(idx)
                total_len += (len(pos_dict[char]) - old_len)
                if total_len >= len(t):
#                    idxes[idx] = pos_dict[next(iter(pos_dict))]
                    moft_left_element = pos_dict[next(iter(pos_dict))][0]
                    if idx - moft_left_element < min_length:
                        min_length = idx - moft_left_element
                        minimal = (moft_left_element, idx)
        if minimal:
            return s[minimal[0]: minimal[1]+1]
        else:
            return ""

#print Solution().minWindow("ADOBECODEBANC", "ABC")
print Solution().minWindow("acbbaca", "aba")
