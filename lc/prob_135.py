class Solution:
    # @param {integer[]} ratings
    # @return {integer}
    def candy(self, ratings):
        results = [1] + [0] * (len(ratings) - 1)
        for i in xrange(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                results[i] = results[i-1] + 1
            elif ratings[i] == ratings[i - 1]:
                results[i] = 1
            else:
                results[i] = 1
                if results[i-1] > 1:
                    pass
                else:
                    idx = i
                    while idx - 1 >= 0 and (ratings[idx - 1] > ratings[idx] and not (results[idx-1] > results[idx])):
                        results[idx - 1] += 1
                        idx -= 1
        #return sum(results)
        print ratings
        print results


Solution().candy([100, 1])