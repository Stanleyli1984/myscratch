class Solution:
    # @param {character[][]} grid
    # @return {integer}
    def numIslands(self, grid):
    
        def get_neighbors(points):
            tmp_set = set()
            for point in points:
                if (point[0], point[1] - 1) in unvisited:
                    tmp_set.add((point[0], point[1] - 1))
                if (point[0] - 1, point[1]) in unvisited:
                    tmp_set.add((point[0] - 1, point[1]))
                if (point[0], point[1] + 1) in unvisited:
                    tmp_set.add((point[0], point[1] + 1))
                if (point[0] + 1, point[1]) in unvisited:
                    tmp_set.add((point[0] + 1, point[1]))
            return tmp_set

        # convert to set
        unvisited = set()
        for i in xrange(len(grid)):
            for j in xrange(len(grid[0])):
                if grid[i][j] == '1':
                    unvisited.add((i, j))

        num_islands = 0                    
        while unvisited:
            num_islands += 1
            neighbors = set()
            neighbors.add(iter(unvisited).next())
            while (neighbors):
                unvisited -= neighbors                
                neighbors = get_neighbors(neighbors)
        return num_islands

print Solution().numIslands(['1'])