class Solution:
    # @return a boolean
    def isMatch(self, s, p):
        return self.recurse(s, p, 0, 0)

    def recurse(self, s, p, pos_s, pos_p):
        if pos_p == len(p):
            return pos_s == len(s)
        char = p[pos_p]
        if pos_p != len(p) - 1 and p[pos_p + 1] == '*':
            if self.recurse(s,p,pos_s,pos_p+2):
                return True
            for x in xrange(pos_s, len(s)):
                if char in [s[x], '.']:
                    if self.recurse(s,p,x+1,pos_p+2):
                        return True
                else:
                    break
        else:
            if pos_s == len(s):
                return False
            if char in [s[pos_s], '.']:
                    return self.recurse(s,p,pos_s + 1,pos_p + 1)
            else:
                return False
        return False

print Solution().isMatch("aaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*c")