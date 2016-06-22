class Solution:
    # @param matrix, a list of lists of integers
    # @return nothing (void), do not return anything, MODIFY matrix IN PLACE.
    def setZeroes(self, matrix):
        first_x, first_y = (None, None)
        for x in xrange(len(matrix)):
            for y in xrange(len(matrix[0])):
                if 0 == matrix[x][y]:
                    first_x = x
                    first_y = y
                    break

        if first_x is None: return
        for x in xrange(len(matrix)):
            if not all([matrix[x][y] for y in xrange(len(matrix[0]))]):
                matrix[x][first_y] = 1
            else:
                matrix[x][first_y] = 0

        for y in xrange(len(matrix[0])):
            if y == first_y:
                continue
            if not all([matrix[x][y] for x in xrange(len(matrix))]):
                matrix[first_x][y] = 1
            else:
                matrix[first_x][y] = 0

        for x in xrange(len(matrix)):
            if x == first_x:
                continue
            if matrix[x][first_y] == 1:
                for y in xrange(len(matrix[0])):
                    matrix[x][y] = 0

        for y in xrange(len(matrix[0])):
            if matrix[first_x][y] == 1:
                for x in xrange(len(matrix)):
                    matrix[x][y] = 0

Solution().setZeroes([[0,1]])