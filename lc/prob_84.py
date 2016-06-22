class Solution:
    # @param {integer[]} height
    # @return {integer}
    def largestRectangleArea(self, height):
        stack = []
        max_area = 0
        height.append(0)
        for idx in xrange(len(height)):
            cal_info = None
            while stack and height[idx] <= stack[-1][1]:
                cal_info = stack.pop()
                new_area = cal_info[1] * (idx - cal_info[0])
                max_area = max_area if new_area <= max_area else new_area
            stack.append((idx, height[idx]) if not cal_info else (cal_info[0], height[idx]))
        return max_area

''' I though about using set to calculate the indxes and heights. But set can't preserve the order.
Using stack can preserve order. Need to use stack more'''

print Solution().largestRectangleArea([2,1,5,6,2,3])