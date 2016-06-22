class Solution:
    # @param {integer[]} nums
    # @return {integer[]}
    def majorityElement(self, nums):
        if len(nums) <= 2:
            return list(set(nums))
        elems = [[float('inf'), 0], [float('inf'), 0]]
        for num in nums:
            if elems[0][0] == num:
                elems[0][1] += 1
                continue

            if elems[1][0] == num:
                elems[1][1] += 1
                continue

            if elems[0][1] == 0:
                elems[0] = [num, 1]
                continue

            if elems[1][1] == 0:
                elems[1] = [num, 1]
                continue

            elems[0][1] -= 1
            elems[1][1] -= 1
        result = []
        if nums.count(elems[0][0]) > len(nums)/3:
            result.append(elems[0][0])
        if nums.count(elems[1][0]) > len(nums)/3:
            result.append(elems[1][0])
        return result

print Solution().majorityElement([3,2,3])