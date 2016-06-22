class Solution:
    # @return a list of lists of string

    def recurse(self, status):
        finished_row = len(status)
        for x in xrange(self.n):
            if x not in status:
                for n in xrange(finished_row):
                    if (finished_row - n) + status[n] == x or -(finished_row - n) + status[n] == x:
                        break
                else:
                    if finished_row == self.n - 1:
                        self.all_results += 1
                    else:
                        self.recurse(status + [x])

    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.n = n
        self.all_results = 0
        self.recurse([])
        #output , like [[0,2,3,1],...]
        return self.all_results

print Solution().totalNQueens(4)