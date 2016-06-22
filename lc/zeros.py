
class Solution:
    # @param {integer} n
    # @return {integer}
    def trailingZeroes(self, n):
        sum_2 = 0
        while n > 0:
            n /= 5
            sum_2 += n
        return sum_2