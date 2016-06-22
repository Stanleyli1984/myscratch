class Solution:
    # @return a list of integers
    def grayCode(self, n):
        if n == 0:
            return [0]
        else:
            return self.grayCode(n-1) + [(2**(n - 1) + x) for x in self.grayCode(n-1)[::-1]]



a = Solution()
print a.grayCode(3)