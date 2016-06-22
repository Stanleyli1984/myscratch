class Solution:
    # @param {string} s
    # @return {boolean}
    def isValid(self, s):
        stack = []
        hash_table = {'}': "{", ']':'[', ')':'('}
        for char in s:
            if char in ('(', '[', '{'):
                stack.append(char)
            elif char in hash_table:
                try:
                    tmp = stack.pop()
                except IndexError:
                    return False
                if hash_table[char] != tmp:
                    return False
        return is hash_table
