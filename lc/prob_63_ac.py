class Solution:
    # @param {integer[][]} obstacleGrid
    # @return {integer}
    def uniquePathsWithObstacles(self, obstacleGrid):
        obstacled = False
        dp_array = []
        for x in obstacleGrid[0]:
            if not obstacled:
                if x:
                    obstacled = True
                    dp_array.append(0)
                else:
                    dp_array.append(1)
            else:
                dp_array.append(0)
        #print dp_array
        for grid_row in obstacleGrid[1:]:
            for col, point in enumerate(grid_row):
                if point:
                    dp_array[col] = 0
                else:
                    if col == 0:
                        pass
                    else:
                        dp_array[col] += dp_array[col-1]
            #print dp_array
        return dp_array[len(obstacleGrid[0])-1]

print Solution().uniquePathsWithObstacles([[0,1,1], [0,0,0]])
