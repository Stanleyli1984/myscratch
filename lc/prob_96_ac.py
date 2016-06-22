class Solution:
    # @return an integer
    def numTrees(self, n):
        total = 0
        if n == 0:
            return 1
        for x in xrange(n):
            total += self.numTrees(x) * self.numTrees(n - 1 - x)
        return total