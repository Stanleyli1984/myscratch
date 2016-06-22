class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLongestSubstring(self, s):
        ptr1 = 0
        ptr2 = 0
        chars = set()
        max_length = 0


        if s[ptr2] in chars:
            chars.remove(s[ptr1])
            ptr1 += 1
        else:
            chars.add(s[ptr2])
            ptr2 += 1
            max_length = ptr2 - ptr1 if (ptr2 - ptr1) > max_length else max_length

