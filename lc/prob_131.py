class Solution:
    # @param {string} s
    # @return {string[][]}
    def partition(self, s):
        self.s = s
        self.results = []
        self.back_trace = []
        self.recr(0)
        return self.results

    def recr(self, start):
        if start == len(self.s):
            self.results.append(list(self.back_trace))
            return
        for loc in xrange(start, len(self.s)):
            part = self.s[start:loc+1]
            if part == part[::-1]:
                self.back_trace.append(part)
                self.recr(loc+1)
                del self.back_trace[-1]

print Solution().partition("cbbbcc")