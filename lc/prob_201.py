class Solution:
    # @param {integer} m
    # @param {integer} n
    # @return {integer}
    def rangeBitwiseAnd(self, m, n):
        diff = n - m
        result = 0
        for i in reversed(xrange(31)):
            if diff >= pow(2, i):
                break
            else:
                mask = 1 << i
                if m & mask == 0 or n & mask == 0:
                    continue
                else:
                    result |= mask
        return result

print Solution().rangeBitwiseAnd(0,0)