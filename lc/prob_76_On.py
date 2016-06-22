class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        map = {}
        for char in t:
            map[char] = map.get(char, 0) + 1

        ptr2 = 0
        valid_cnt = 0
        char_map = {}
        min_length = float('inf')
        min_range = None
        for ptr1 in xrange(len(s)):
            if s[ptr1] not in map:
                continue
            char_map[s[ptr1]] = char_map.get(s[ptr1], 0) + 1
            if char_map[s[ptr1]] <= map[s[ptr1]]:
                valid_cnt += 1
            if valid_cnt == len(t):
                while True:
                    if s[ptr2] in char_map:
                        if char_map[s[ptr2]] == map[s[ptr2]]:
                            if ptr1 - ptr2 < min_length:
                                min_length = ptr1 - ptr2
                                min_range = (ptr2, ptr1)
                            break
                        else: #char_map[s[ptr2]] > map[s[ptr2]]:
                            char_map[s[ptr2]] -= 1
                            ptr2 += 1
                    else:
                        ptr2 += 1
        if min_range:
            return s[min_range[0]: min_range[1] + 1]
        else:
            return ""

print Solution().minWindow("assa", "aa")