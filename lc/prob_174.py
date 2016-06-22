class Solution:
    # @param {integer[][]} dungeon
    # @return {integer}
    def calculateMinimumHP(self, dungeon):
        dp_array = [float('inf')] * len(dungeon[0])
        for idx, row in enumerate(reversed(dungeon)):
            if idx == 0:
                new_dp_array = [None] * len(dungeon[0]) + [1]
            else:
                new_dp_array = [None] * len(dungeon[0]) + [float('inf')]
            for i in xrange(len(dungeon[0]) - 1, -1, -1):
                new_dp_array[i] = min(dp_array[i], new_dp_array[i+1]) - row[i]
                if new_dp_array[i] < 1:
                    new_dp_array[i] = 1
            dp_array = new_dp_array
        return dp_array[0]

print Solution().calculateMinimumHP([[-2, -3,3], [-5,-10,1], [10, 30,-5]])
