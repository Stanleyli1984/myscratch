class Solution:
    # @return an integer
    # S = "rabbbit", T = "rabbit"
    def numDistinct(self, S, T):
        self.sum = 0
        if len(S) < len(T) or not S or not T:
            return 0
        self.traverseStr(S,T,0,0)
        return self.sum

    def traverseStr(self, S, T, pos_S, pos_T):
        if pos_T == len(T) - 1:
            self.sum += S[pos_S:].count(T[-1])
            return
        #for idx in xrange(pos_S, len(S) - (len(T) - pos_T -1)):
        #    if S[idx] == T[pos_T]:
        for idx in [i+pos_S for i, x in enumerate(S[pos_S:-(len(T) - pos_T - 1)]) if x == T[pos_T]]:
        #for idx in [i+pos_S for i, x in enumerate(S[pos_S:]) if x == T[pos_T]]:
            self.traverseStr(S , T, idx+1, pos_T + 1)

print Solution().numDistinct("daacaedaceacabbaabdccdaaeaebacddadcaeaacadbceaecddecdeedcebcdacdaebccdeebcbdeaccabcecbeeaadbccbaeccbbdaeadecabbbedceaddcdeabbcdaeadcddedddcececbeeabcbecaeadddeddccbdbcdcbceabcacddbbcedebbcaccac", "ceadbaa")