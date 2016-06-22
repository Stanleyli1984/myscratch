__author__ = 'zhongqil'


class Solution:
    # @param {integer[][]} matrix
    # @param {integer} target
    # @return {boolean}
    def searchMatrix(self, matrix, target):
        if not matrix:
            return False
        header_l = [x[0] for x in matrix]
        found, row = self.binarysearch(header_l, target)
        if found:
            return True
        else:
            found, row = self.binarysearch(matrix[row], target)
            return found

    def binarysearch(self, l, target):
        start = 0
        end = len(l) - 1
        while (start < end): # at least two elements
            middle_pos = (start + end) / 2
            middle = l[middle_pos]
            if target == middle:
                return True, middle_pos
            elif target > middle:
                if target < l[middle_pos + 1]:
                    return False, middle_pos
                start = middle_pos + 1
            else:
                end = middle_pos - 1
        return l[start] == target, start

print Solution().searchMatrix([[1,2,3], [4,5,6], [7,8,9]], 4)