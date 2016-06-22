class Solution:
    # @param {string} word1
    # @param {string} word2
    # @return {integer}
    def minDistance(self, word1, word2):
        dp_array = [float('-inf')] + [float('inf')] * (len(word2)) # At least how many chars are needed to generate inx number of matches
        # Find the maximal number of matches
        for char1 in word1:
            for idx2, char2 in enumerate(word2):
                if char1 == char2:
                    for i in xrange(1, len(dp_array)):
                        if dp_array[i-1] < idx2:
                            if dp_array[i] > idx2:
                                dp_array[i] = idx2
                        else:
                            break
        #print dp_array
        idx1 = 0
        for idx, v in enumerate(dp_array):
            if v != float('inf'):
                idx1 = idx
            else:
                break
        #print idx1
        return abs(len(word1)-len(word2)) + min(len(word1), len(word2)) - idx1

print Solution().minDistance("ab", "bc")