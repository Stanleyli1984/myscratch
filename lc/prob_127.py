import operator

class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return an integer

    def is_neighbor(self, in1, in2):
        return sum(map(operator.ne, in1, in2)) == 1

    def ladderLength(self, start, end, dict):
        unvisited = dict
        distance = 0
        this_batch = set([start])
        #print this_batch
        while(1):
            distance += 1
            next_batch = set()
            for v_word in this_batch:
                if self.is_neighbor(end, v_word):
                    return distance
                for un_word in set(unvisited):
                    if self.is_neighbor(v_word, un_word):
                        next_batch.add(un_word)
                        unvisited.remove(un_word)
            if not next_batch:
                return 0
            this_batch = next_batch



print Solution().ladderLength("hot", "dog", set(["hot","dog"]))