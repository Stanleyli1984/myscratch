class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        tokens = []
        prev = None
        for char in s:
            if char == ' ':
                continue
            if char in ('(', ')', '-', '+'):
                if prev is not None:
                    tokens.append(prev)
                    prev = None
                tokens.append(char)
            else:
                if prev is None:
                    prev = int(char)
                else:
                    prev = 10 * prev + int(char)
        if prev is not None:
            tokens.append(prev)

        stack = [None]
        for token in tokens:
            if token == '(':
                stack.append(None)
                continue
            if token in ('+', '-'):
                stack[-1].append(token)
                continue
            if token == ')':
                if stack[-2][-1] == '+':
                    del stack[-2][-1]
                    stack[-2][-1] += stack[-1][0]
                if stack[-2][-1] == '-':
                    del stack[-2][-1]
                    stack[-2][-1] -= stack[-1][0]
                del stack[-1]
                continue
            if token is int:
                if stack[-1][-1] == '+':
                    del stack[-1][-1]
                    stack[-1][-1] += token
                elif stack[-1][-1] == '-':
                    del stack[-1][-1]
                    stack[-1][-1] -= token
                else:
                    stack[-1].append(token)
        return stack[-1][0]




