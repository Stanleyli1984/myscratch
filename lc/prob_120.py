class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):
        if len(triangle) == 1:
            return triangle[0][0]
        for row in xrange(1, len(triangle)):
            for column in xrange(len(triangle[row])):
                if column == 0:
                    triangle[row][column] += triangle[row - 1][column]
                elif column == len(triangle[row]) - 1:
                    triangle[row][column] += triangle[row - 1][column - 1]
                else:
                    triangle[row][column] += min(triangle[row - 1][column - 1], triangle[row - 1][column])
        return min(triangle[len(triangle) - 1])