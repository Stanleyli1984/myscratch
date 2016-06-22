class Solution:
    # @return a list of lists of integers

    def __init__(self):
        self.results = []
        self.current = []

    def combine(self, n, k):
        if not k:
            return []
        self.recurse(1, n, k)
        return self.results

    def recurse(self, starting, ending, remaining):
        if remaining == 1:
            for x in xrange(starting, ending + 1):
                self.results.append(self.current + [x])
            return
        for x in xrange(starting, ending + 1):
            self.current.append(x)
            self.recurse(x + 1, ending, remaining - 1)
            self.current.pop()

print Solution().combine(4,2)