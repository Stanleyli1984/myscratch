class Solution:
    # @param {string} s
    # @return {boolean}
    def isPalindrome(self, s):
        s1 = [x.lower() for x in s if x.isalnum()]
        return s1 == s1[::-1]