class Solution:
    # @param {integer} n
    # @return {string}
    def convertToTitle(self, n):
        result = ""
        A_code = ord('A')
        while (n > 0):
            n, mod = divmod(n - 1, 26)
            result = chr(A_code + mod) + result
        return result

print Solution().convertToTitle(10000)