class Solution:
    # @return an integer
    # S = "rabbbit", T = "rabbit"
    def numDistinct(self, S, T):
        self.sum = 0
        if len(S) < len(T) or not S or not T:
            return 0
        
        D = [0] * len(T)
        
        #for n in xrange(len(S)):
        #    D = [[0 for x in xrange(len(T))] for y in xrange(len(S))]
        
        D[0] = 1 if T[0] == S[0] else 0
        for m in xrange(1, len(S)):
            for n in xrange(len(T) - 1, 0, -1):
                if (S[m] == T[n]):
                    D[n] = D[n-1] + D[n]
            D[0] = S[:m+1].count(T[0])
                    
        return D[-1]
            