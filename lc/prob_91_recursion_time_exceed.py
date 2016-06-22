import cProfile
class Solution:
    # @param s, a string
    # @return an integer
    def __init__(self):
        self.result = 0

    def numDecodings(self, s):
        if not s: return 0
        self.recurse(0,s)
        return self.result

    def recurse(self, position, s):
        if position == '0':
            return
        if position == len(s) - 1:
            self.result += 1
            return
        if position == len(s) - 2:
            if s[-2] == '1' or (s[-2] == '2' and s[-1] <= '6'):
                self.result += 1
            self.recurse(position + 1, s)
            return
        self.recurse(position + 1, s)
        if s[position] == '1' or (s[position] == '2' and s[position + 1] <= '6'):
            self.recurse(position + 2, s)

cProfile.run("print Solution().numDecodings(\"4757562545844617494555774581341211511296816786586787755257741178599337186486723247528324612117156948\")")
