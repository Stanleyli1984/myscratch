class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {integer}
    def findKthLargest(self, nums, k):
        self.nums = nums
        pos = -1
        prev_start = 0
        prev_end = len(nums) - 1
        while True:
            pos = self.quicksort(prev_start, prev_end)
            if pos == k - 1:
                return self.nums[pos]
            elif pos  > k - 1:
                prev_end = pos - 1
            else:
                prev_start = pos + 1

    def quicksort(self, start, end):
        if start == end:
            return start
        pivot = (start + end) /2
        self.nums[end], self.nums[pivot] = self.nums[pivot], self.nums[end]
        store_ptr = start
        for idx in xrange(start, end):
            if self.nums[idx] > self.nums[end]:
                self.nums[idx], self.nums[store_ptr] = self.nums[store_ptr],self.nums[idx]
                store_ptr += 1
        self.nums[store_ptr], self.nums[end] =  self.nums[end], self.nums[store_ptr]
        return store_ptr

print Solution().findKthLargest([5,1,6,4,4], 5)