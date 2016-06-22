from collections import deque

class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {integer[]}
    def maxSlidingWindow(self, nums, k):
        queue = deque()
        results = []
        for idx, num in enumerate(nums):
            for q_idx, q_num in reversed(list(queue)):
                if q_num <= num:
                    queue.pop()
                else:
                    queue.append((idx, num))
                    break
            else:
                queue.append((idx, num))
            if queue[0][0] <= idx - k:
                queue.popleft()
            if idx >= k - 1:
                results.append(queue[0][1])
        return results

print Solution().maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3)