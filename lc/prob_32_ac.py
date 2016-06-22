class Solution:
    # @param {string} s
    # @return {integer}
    def longestValidParentheses(self, s):
        if not s:
            return 0
        longest_num = 0
        curr_num = 0
        left_paren = 0
        for char in s:
            if char == '(':
                left_paren += 1
                curr_num += 1
            else:
                left_paren -= 1
                if left_paren == 0:
                    curr_num += 1
                    if curr_num > longest_num:
                        longest_num = curr_num
                elif left_paren < 0:
                    left_paren = 0
                    curr_num = 0
                else:
                    curr_num += 1
        curr_num = 0
        left_paren = 0
        for char in reversed(s):
            if char == ')':
                left_paren += 1
                curr_num += 1
            else:
                left_paren -= 1
                if left_paren == 0:
                    curr_num += 1
                    if curr_num > longest_num:
                        longest_num = curr_num
                elif left_paren < 0:
                    left_paren = 0
                    curr_num = 0
                else:
                    curr_num += 1
        return longest_num

print Solution().longestValidParentheses(")(()(()()")
print Solution().longestValidParentheses(")()())")
print Solution().longestValidParentheses("()")