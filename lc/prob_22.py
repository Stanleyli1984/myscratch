class Solution:
    # @param an integer
    # @return a list of string

    def generateParenthesis(self, n):
        self.total_num = n * 2
        self.current = [None] * self.total_num
        self.all_strs = []
        if n == 0:
            return []
        self.Traverse(0,0)
        return self.all_strs


    def Traverse(self, left_num, right_num):
        if left_num + right_num == self.total_num - 1:
            self.current[self.total_num - 1] = ')'
            self.all_strs.append(reduce(lambda x, y : x+y, self.current))
            return
        if left_num < self.total_num / 2:
            self.current[left_num + right_num] = '('
            self.Traverse(left_num + 1, right_num)
        if right_num < self.total_num / 2 and left_num > right_num:
            self.current[left_num + right_num] = ')'
            self.Traverse(left_num, right_num + 1)

print Solution().generateParenthesis(3)