class Solution:
    # @return an integer
    def reverse(self, x):
        result = 0
        sign = 1
        if (x < 0):
            sign = -1
            x = -x
        while(x):
            if (result * 10 + x%10 > 0x7FFFFFFF): # Python doesn't have the overflow issue. Just to make the test pass
                return 0
            result = result * 10 + x%10
            x/=10
        return result * sign