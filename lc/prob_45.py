class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def jump(self, nums):
        dp_array = [0] + [float('inf')] * (len(nums) - 1)
        for idx, num in enumerate(nums):
            if idx == len(nums) - 1:
                return dp_array[-1]
            for idx1 in xrange(min(len(nums)-1, idx + num), idx, -1):
                tmp = dp_array[idx] + 1
                if dp_array[idx1] > tmp:
                    dp_array[idx1] = tmp
                elif idx1 == len(nums)-1:
                    return dp_array[idx1]
                else:
                    break
            #print dp_array
#print Solution().jump([1,1,2])
print Solution().jump([35,34,33,32,31,30,29,28,27,26,25,24,23,22,21,20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1,1,0])