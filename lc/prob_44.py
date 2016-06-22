class Solution:
    # @param {string} s
    # @param {string} p
    # @return {boolean}
    def isMatch(self, s, p):
        array = [1] + [0] * len(s)
        for p_char in p:
            if not any(array):
                return False
            new_array = [0] * (len(s) + 1)
            if p_char == '*':
                for i in xrange(array.index(1), len(array)):
                    new_array[i] = 1
            if p_char == '?':
                for i in xrange(array.index(1), len(array)-1):
                    if array[i] == 1:
                        new_array[i+1] = 1
            else:
                for i in xrange(array.index(1), len(array)-1):
                    if array[i] == 1 and s[i] == p_char:
                        new_array[i+1] = 1
            array = new_array
        return True if array[-1] else False



