class Solution(object):
    def b_search(self, array, val):
        start = 0
        end = len(array) - 1
        while start < end - 1:
            cur = (start + end) / 2
            if array[cur] <= val:
                start = cur
            else:
                end = cur
        return end

    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        datas = [[nums[0]]]
        last_elements = []
        for num in nums:
            if num <= datas[0][0]:
                continue
            if num > datas[-1][-1]:
                datas.append(datas[-1] + [num])
                continue
            pos = self.b_search(last_elements, num)
            if num < datas[pos][-1]:
                datas[pos] = datas[pos][1:-1] + [num]
        return len(datas[-1])
