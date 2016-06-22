#import itertools

class Solution:
    # @param s, a string
    # @return a list of strings
    def restoreIpAddresses(self, s):
        all_strings = []
        for x in self.generateIPs(s, 4):
            #y = list(itertools.chain.from_iterable(x))
            all_strings.append('.'.join(x))
        return all_strings


    def generateIPs(self, s, segs):
            if segs == 1:
                if not s or int(s) > 255:
                    return [[]]
                if s[0] == '0' and len(s) >= 2:
                    return [[]]
                else:
                    return [[s]]
            else:
                all_lists = []
                for x in xrange(1,4):
                    for (seg1, seg2) in ((i,j) for i in self.generateIPs(s[0:x], 1) if i for j in self.generateIPs(s[x:len(s)], segs - 1) if j):
                          all_lists.append(seg1 + seg2)
                    #a = [self.generateIPs(s[0:x + 1], 1), self.generateIPs(s[x+1:len(s)], segs - 1)]
                    #tmp = list(itertools.product(*a))
                    #all_lists.extend(tmp)
                return all_lists

