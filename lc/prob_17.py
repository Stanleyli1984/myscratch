class Solution:
    # @return a list of strings, [s1, s2]
    def letterCombinations(self, digits):
        table = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        prevs = [""]
        currents = []
        for digit in digits:
            currents = []
            for prev in prevs:
                for char in table[digit]:
                    currents.append(prev + char)
            prevs = currents
        return currents
