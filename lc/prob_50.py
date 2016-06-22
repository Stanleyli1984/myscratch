class Solution:
    # @param {float} x
    # @param {integer} n
    # @return {float}
    def myPow(self, x, n):
        self.h_table = {0:1, 1:x, 2:x*x}
        self.x = x
        if n == 0:
            return 1
        if n < 0:
            return 1.0/self.recurs(-n)
        else:
            return self.recurs(n)

    def recurs(self, n):
        if n in self.h_table:
            return self.h_table[n]
        m, d = divmod(n, 2)
        result = self.recurs(m)
        self.h_table[m] = result
        return result * result * (1 if d == 0 else self.x)

print Solution().myPow(2, 3)