class Solution:
    # @param {integer} n
    # @param {integer} k
    # @return {string}
    def getPermutation(self, n, k):
        result = []
        m = k - 1
        all_l = list(xrange(1, n+1))
        total_num = reduce(lambda x, y: x * y, all_l)
        for step in xrange(n, 1, -1):
            total_num /= step
            d, m = divmod(m, total_num)
            result.append(all_l[d])
            del all_l[d]
        return ''.join([str(x) for x in (result + all_l)])

print Solution().getPermutation(3, 6)