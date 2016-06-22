class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        words = s.strip().split()
        return ' '.join([x for x in reversed(words)])