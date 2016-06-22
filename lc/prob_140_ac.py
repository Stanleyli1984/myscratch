class Solution:
    # @param s, a string
    # @param wordDict, a set<string>
    # @return a string[]

    def wordBreak(self, s, wordDict):
        self.results = []
        self.dict_set = set(wordDict)
        self.s = s
        self.possibles = {}
        self.feasibles = [True] * len(s)
        self.length = len(s)
        self.recur([0])
        return self.results

    def recur(self, spaces):
        pos = spaces[-1]
        if pos not in self.possibles:
            tmp = []
            for end in xrange(pos + 1, self.length + 1):
                if self.s[pos:end] in self.dict_set:
                    tmp.append(end)
            self.possibles[pos] = tmp
        found = False
        for end in self.possibles[pos]:
            if end == self.length:
                prev = spaces.pop(0)
                result = []
                for cur in spaces:
                    result.append(self.s[prev:cur])
                    prev = cur
                result.append(self.s[prev:])
                self.results.append(' '.join(result))
                return True
            else:
                if self.feasibles[end]:
                    if self.recur(spaces + [end]):
                        found = True
                    else:
                        self.feasibles[end] = False
        return found

print Solution().wordBreak("aaaaaaaaaab", ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"])