class Solution:
    # @param {integer} k
    # @param {integer} n
    # @return {integer[][]}
    def combinationSum3(self, k, n):
        self.sums = (0, 1, 3, 6, 10, 15, 21, 28, 36, 45)
        self.backtrace = []
        self.results = []
        self.recr(k, n, 9)
        return [list(reversed(x)) for x in self.results]

    def recr(self, remaing_num, remaing_sum, largest):
        if largest < remaing_num:
            return
        elif largest == remaing_num:
            if self.sums[remaing_num] == remaing_sum:
                self.results.append(self.backtrace + list(xrange(remaing_num, 0, -1)))
            else:
                return
        else:
            if remaing_num == 1:
                if largest >= remaing_sum:
                    self.results.append(self.backtrace + [remaing_sum])
            else:
                for i in xrange(remaing_num, min(remaing_sum - self.sums[remaing_num-1] + 1, largest+1)):
                    self.backtrace.append(i)
                    self.recr(remaing_num-1, remaing_sum - i, i - 1)
                    del self.backtrace[-1]

print Solution().combinationSum3(3, 9)