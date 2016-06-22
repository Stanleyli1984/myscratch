class Solution:
    # @param s, a string
    # @return an integer
    def numDecodings(self, s):
        if not s: return 0
        statuses = []
        for pos in xrange(len(s)):
            statuses.append(0)
            if s[pos] != '0':
                if pos == 0:
                    statuses[0] += 1
                else:
                    statuses[pos] += statuses[pos - 1]
            if pos >= 1:
                if s[pos - 1] == '1' or (s[pos - 1] == '2' and s[pos] <= '6'):
                    if pos == 1:
                        statuses[1] += 1
                    else:
                        statuses[pos] += statuses[pos - 2]
        return statuses[len(s) - 1]

print Solution().numDecodings('11')