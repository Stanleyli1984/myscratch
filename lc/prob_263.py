class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 0:
            return False
        q = num
        for factor in (2,3,5):
            while True:
                if q == 1:
                    return True
                tmp, m = divmod(q, factor)
                if m == 0:
                    q = tmp
                else:
                    break
        return False

print Solution().isUgly(1)