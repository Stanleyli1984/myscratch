class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):
        start = -1
        if not s:
            return 0
        for idx, val in enumerate(reversed(s)):
            if start == -1 and val != ' ':
                start = idx

            if val == ' ' and start != -1:
                return idx - start
        if start != -1:
            return len(s) - start
        return 0
