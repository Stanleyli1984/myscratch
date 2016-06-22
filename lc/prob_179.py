class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        def cmp_str(x, y):
            return int(y + x) - int(x + y)

        if not nums:
            return None
        nums_str = [str(x) for x in nums]
        sorted_num_str = sorted(nums_str, cmp=cmp_str)
        result = ''.join(sorted_num_str)
        first_non_zero_pos = -1
        for idx, char in enumerate(result):
            if char != '0':
                first_non_zero_pos = idx
                break
        return result[first_non_zero_pos:]

print Solution().largestNumber([0, 0])