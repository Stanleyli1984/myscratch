class Solution:
    # @param S, a list of integer
    # @return a list of lists of integer

    def __init__(self):
        self.results = []
        self.current = []
    def subsets(self, S):
        S.sort()
        for length in xrange(len(S) + 1):
            if length == 0:
                self.results.append([])
                continue
            self.recurse(0, length, S)
        return self.results

    def recurse(self, start, length, S):
        if length == 1:
            for idx in xrange(start, len(S)):
                self.results.append(self.current + [S[idx]])
            return
        for idx in xrange(start, len(S)):
            self.current.append(S[idx])
            self.recurse(idx + 1, length - 1, S)
            self.current.pop()

print Solution().subsets([1,2,3])
