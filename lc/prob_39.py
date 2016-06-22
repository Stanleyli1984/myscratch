class Solution:
    # @param {integer[]} candidates
    # @param {integer} target
    # @return {integer[][]}

    def combinationSum(self, candidates, target):
        self.results = []
        self.candidates = sorted(candidates)
        self.recurs(0, [], target)
        return self.results

    def recurs(self, idx, cur_list, remaining):
        for idx1, candidate in enumerate(self.candidates[idx:]):
            if candidate > remaining:
                break
            else:
                new_list = cur_list + [candidate]
                if candidate == remaining:
                    self.results.append(new_list)
                    break
                else:
                    self.recurs(idx1 + idx, new_list, remaining - candidate)

print Solution().combinationSum([2,3,5], 8)