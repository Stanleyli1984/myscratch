# Look at it again!!!!!!!!!!!

class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        #print 'here'
        if len(s) == 0:
            return ""
        full_s = s + '#' + s[::-1]
        table = [0] * len(full_s)
        for i in xrange(1, len(table)):
            value = table[i-1]
            while value > 0 and full_s[value] != full_s[i]:
                 value = table[value - 1]
            if full_s[i] == full_s[value]:
                table[i] = value + 1
            else:
                table[i] = 0
            print table

        if table[-1] > len(s):
            return s
        else:
            return s[::-1][:len(s) - table[-1]] + s

print Solution().shortestPalindrome('aacecaaa')
#print Solution().shortestPalindrome('aab')
        