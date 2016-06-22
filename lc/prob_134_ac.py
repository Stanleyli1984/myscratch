class Solution:
    # @param {integer[]} gas
    # @param {integer[]} cost
    # @return {integer}
    def canCompleteCircuit(self, gas, cost):
        if sum(gas) < sum(cost):
            return -1

        i = 0
        aux_gas = gas + gas
        aux_cost = cost + cost
        while i < len(gas):
            tmp = 0
            for j in xrange(i, i + len(gas)):
                tmp += aux_gas[j] - aux_cost[j]
                if tmp < 0:
                    i = j + 1
                    break
                elif j == i + len(gas) - 1:
                    return i
        return -1
