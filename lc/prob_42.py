class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        stack = []
        result = 0
        for idx, h in enumerate(height):
            if not stack:
                stack.append((idx, h, 0))
            else:
                left = stack[0]
                ex_sum = 0
                for h_stack in reversed(stack):
                    if h_stack[1] <= h:
                        ex_sum += h_stack[2] + h_stack[1]
                        stack.pop()
                    else:
                        break
                if stack:
                    stack.append((idx, h, ex_sum))
                else:
                    result += left[1] * (idx - left[0]) - ex_sum
                    stack.append((idx, h, 0))

        for idx in xrange(1,len(stack)):
            result += stack[idx][1] * (stack[idx][0] - stack[idx-1][0] - 1) - stack[idx][2]
        return result

print Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1])