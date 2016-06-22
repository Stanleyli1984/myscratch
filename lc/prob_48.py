class Solution:
    # @param {integer[][]} matrix
    # @return {void} Do not return anything, modify matrix in-place instead.
    def rotate(self, matrix):
        n = len(matrix)
        if n % 2 == 0:
            x = y = n/2
        else:
            x = n/2
            y = n/2+1
        for i in xrange(x):
            for j in xrange(y):
                matrix[i][j], matrix[j][n -1-i],matrix[n-1-i][n-1-j],matrix[n-1-j][i] = \
                    matrix[n-1-j][i], matrix[i][j], matrix[j][n -1-i],matrix[n-1-i][n-1-j]

print Solution().rotate([[1]])
