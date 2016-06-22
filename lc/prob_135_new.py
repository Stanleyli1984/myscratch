class Solution:
    # @param {integer[]} ratings
    # @return {integer}
    def candy(self, ratings):
        scores = [[None] * (len(ratings)), [None] * (len(ratings))]
        for l_idx, l in enumerate((ratings, ratings[::-1])):
            for idx, rating in enumerate(l):
                if idx > 0 and rating > l[idx - 1]:
                    scores[l_idx][idx] = scores[l_idx][idx - 1] + 1
                else:
                    scores[l_idx][idx] = 1

        f_l = [max(x, y) for x, y in zip(scores[0], scores[1][::-1])]
        return sum(f_l)

print Solution().candy([2,3,2])