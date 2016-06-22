class NumMatrix(object):
    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """
        self.m = [[0] * (len(matrix[0]) + 1)]
        for r in matrix:
            self.m.append([0])
            for idx, num in enumerate(r):
                self.m[-1].append(self.m[-1][-1] + self.m[-2][idx+1] - self.m[-2][idx] + num)
        print self.m

    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return self.m[row2+1][col2+1]-self.m[row2+1][col1]-self.m[row1][col2+1]+self.m[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
numMatrix = NumMatrix([[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]])
print numMatrix.sumRegion(2,1,4,3)
numMatrix.sumRegion(1, 2, 3, 4)