class Solution:
    # @param {integer[]} candidates
    # @param {integer} target
    # @return {integer[][]}

    def combinationSum2(self, candidates, target):
        self.results = set()
        self.candidates = sorted(candidates)
        self.length = len(self.candidates)
        self.cur_list = []
        self.recurs(0, target)
        return list(self.results)

    def recurs(self, idx, remaining):
        for idx1 in xrange(idx, self.length):
            candidate = self.candidates[idx1]
            if candidate > remaining:
                break
            else:
                if candidate == remaining:
                    self.results.add(tuple(self.cur_list + [candidate]))
                    break
                else:
                    self.cur_list.append(candidate)
                    self.recurs(idx1 + 1,remaining - candidate)
                    del self.cur_list[-1]
