class Solution:
    # @return a list of lists of string

    def recurse(self):
        finished_row = len(self.status)
        for x in xrange(self.n):
            if x not in self.status:
                can_place = True
                for n in xrange(finished_row):
                    if (finished_row - n) + self.status[n] == x or -(finished_row - n) + self.status[n] == x:
                        can_place = False
                        break
                if can_place:
                    if finished_row == self.n - 1:
                        self.all_results.append(self.status + [x])
                    else:
                        self.status.append(x)
                        self.recurse()
                        self.status.pop()

    def solveNQueens(self, n):
        self.n = n
        self.status = []
        self.all_results = []
        self.recurse()
        #output , like [[0,2,3,1],...]
        results = []
        for one_result in self.all_results:
            s_result = []
            for x in one_result:
                s_result.append('.' * x + 'Q' + '.' * (n - x - 1))
            results.append(s_result)
        return results

print Solution().solveNQueens(8)