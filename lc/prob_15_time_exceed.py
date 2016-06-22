class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, num):
        results = []
        number_dict = {}
        for x in num:
            if x in number_dict:
                if x == 0:
                    number_dict[0] += 1
                else:
                    if number_dict[x] < 2:
                        number_dict[x] = 2
            else:
                number_dict[x] = 1
        pos_set = []
        neg_set = []
        for k, v in number_dict.iteritems():
            if k < 0:
                neg_set.extend([k] * v)
            if k > 0:
                pos_set.extend([k] * v)
        neg_set.sort()
        pos_set.sort()
        for idx1 in xrange(len(neg_set)):
            for idx2 in xrange(idx1 + 1, len(neg_set)):
                if -neg_set[idx1]-neg_set[idx2] in pos_set:
                    results.append([neg_set[idx1], neg_set[idx2], -neg_set[idx1]-neg_set[idx2]])
        for idx1 in xrange(len(pos_set)):
            for idx2 in xrange(idx1 + 1, len(pos_set)):
                if -pos_set[idx1]-pos_set[idx2] in neg_set:
                    results.append([ -pos_set[idx1]-pos_set[idx2], pos_set[idx1], pos_set[idx2]])

        if 0 in number_dict:
            for v in set(neg_set):
                if -v in pos_set:
                    results.append([v, 0, -v])

        if number_dict.get(0, 0) >= 3:
            results.append([ 0, 0, 0])
        return results

print Solution().threeSum([-1, 0, 1, 2, -1, -4])