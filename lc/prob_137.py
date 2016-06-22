class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        zeros = pow(2,32)-1
        ones = twos = 0
        for num in nums:
            n_num = ~num
            zeros, ones, twos = (twos & num | zeros & n_num), (zeros & num) | (ones & n_num), (ones & num) | (twos & n_num)
        if ones <= pow(2,31)-1:
            return ones
        else:
            return -(pow(2,31) - (ones - pow(2,31)))

print Solution().singleNumber([-1, -1, -1, -4])
