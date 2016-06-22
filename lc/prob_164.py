class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def maximumGap(self, nums):
        if len(nums) < 2:
            return 0
        min_num = min(nums)
        max_num = max(nums)
        array = [None] * (len(nums) + 1)
        for idx, num in enumerate(nums):
            new_idx = int((num - min_num) / float(max_num - min_num) * len(nums))
            if not array[new_idx]:
                array[new_idx] = [num, num]
            elif num < array[new_idx][0]:
                array[new_idx][0] = num
            elif num > array[new_idx][1]:
                array[new_idx][1] = num

        max_gap = 0
        last_max = min_num
        for idx, elem in enumerate(array):
            if elem:
                if elem[0] - last_max > max_gap:
                    max_gap = elem[0] - last_max
                last_max = elem[1]
        return max_gap

print Solution().maximumGap([8,1,2,50000,100000])