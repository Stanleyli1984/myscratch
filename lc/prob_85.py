class Solution:
    # @param {character[][]} matrix
    # @return {integer}
    def maximalRectangle(self, matrix):
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        height = [0] * len(matrix[0])
        heights = []
        for row in xrange(len(matrix)):
            for col in xrange(len(matrix[0])):
                if matrix[row][col] == '1':
                    height[col] += 1
                else:
                    height[col] = 0
            heights.append(list(height))
        areas = [self.largestRectangleArea(x) for x in heights]
        return max(areas)

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

print Solution().maximalRectangle(["10","10"])