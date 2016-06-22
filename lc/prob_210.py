class Solution:
    # @param {integer} numCourses
    # @param {integer[][]} prerequisites
    # @return {integer[]}
    def findOrder(self, numCourses, prerequisites):
        self.pre_dict = {}
        self.sorted_nodes = []
        for x in xrange(numCourses):
            self.pre_dict[x] = []
        for item in prerequisites:
            self.pre_dict[item[0]].append(item[1])
        self.unvisited = set(xrange(numCourses))
        self.back_trace = set()
        while self.unvisited:
            if not self.recr(next(iter(self.unvisited))):
                return []
        return self.sorted_nodes

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
        self.sorted_nodes.append(node)
        return True

print Solution().findOrder(4, [[1,0],[2,0],[3,1],[3,2]])