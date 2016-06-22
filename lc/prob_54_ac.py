class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of integers
    def spiralOrder(self, matrix):
        if not matrix:
            return []
        h = len(matrix) - 1
        w = len(matrix[0]) - 1

        result = []
        k = 0
        while (1):
            if w - k >= k:
                result.extend(matrix[k][k:w-k + 1])
            else:
                break

            if h - k >= k + 1:
                for i in xrange(k + 1 , h - k + 1):
                    result.append(matrix[i][-k-1])
            else:
                break

            if k <= w - k - 1:
                result.extend(matrix[h - k][w- k - 1:(None if k - 1 < 0 else k -1) : -1])
            else:
                break

            if h - 1 - k >= k + 1:
                for i in xrange(h - 1 - k, k, -1):
                    result.append(matrix[i][k])
            else:
                break
            k += 1
        return result

print Solution().spiralOrder([[5, 6,0,3], [2,3,4,6],[7,8,9,1], [10, 11, 12, 13]])