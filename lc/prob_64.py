class Solution:
    # @param {integer[][]} grid
    # @return {integer}
    def minPathSum(self, grid):
        dp_array = list(grid[0])
        for i in xrange(1, len(grid[0])):
            dp_array[i] += dp_array[i - 1]
        for row in grid[1:]:
            dp_array[0] += row[0]
            for i in xrange(1, len(dp_array)):
                dp_array[i] = row[i] + (dp_array[i - 1] if dp_array[i - 1] < dp_array[i] else dp_array[i])
        return dp_array[-1]