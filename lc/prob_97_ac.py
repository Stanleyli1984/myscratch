__author__ = 'zhongqil'


class Solution:
    # @param {string} s1
    # @param {string} s2
    # @param {string} s3
    # @return {boolean}
    def isInterleave(self, s1, s2, s3):
        possible_combs = [0]
        if len(s1) + len(s2) != len(s3):
            return False
        for idx, char_3 in enumerate(s3):
            #print idx, char_3, possible_combs
            new_possible_combs = set()
            for possible_comb in possible_combs:
                if possible_comb < len(s1) and char_3 == s1[possible_comb]:
                    new_possible_combs.add(possible_comb + 1)
                if idx - possible_comb < len(s2) and char_3 == s2[idx - possible_comb]:
                    new_possible_combs.add(possible_comb)
            #print new_possible_combs
            if not new_possible_combs:
                return False
            else:
                possible_combs = new_possible_combs
        return True

#print Solution().isInterleave("aabcc", "dbbca", "aadbbbaccc")
print Solution().isInterleave("a", "b", "a")