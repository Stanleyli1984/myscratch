class Solution:
    # @param {integer} numCourses
    # @param {integer[][]} prerequisites
    # @return {boolean}
    def canFinish(self, numCourses, prerequisites):
        self.pre_dict = {}
        for x in xrange(numCourses):
            self.pre_dict[x] = []
        for item in prerequisites:
            self.pre_dict[item[0]].append(item[1])
        self.unvisited = set(xrange(numCourses))
        self.back_trace = set()
        while self.unvisited:
            if not self.recr(next(iter(self.unvisited))):
                return False
        return True

    def recr(self, node):
        if node in self.back_trace:
            return False
        self.back_trace.add(node)
        for child in self.pre_dict[node]:
            if child in self.unvisited:
                if not self.recr(child):
                    return False
        self.unvisited.remove(node)
        self.back_trace.remove(node)
        return True

print Solution().canFinish(2, [[0, 1]])