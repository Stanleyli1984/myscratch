import operator

class node_class:
    def __init__(self, word, distance = float("inf")):
        self.distance = distance
        self.visited = 0
        self.word = word

class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return an integer

    def is_neighbor(self, in1, in2):
        distance = sum(map(operator.ne, in1, in2))
        return (distance == 1)

    def ladderLength(self, start, end, dict):
        nodes = [node_class(start, 0)]
        for word in dict:
            nodes.append(node_class(word))
        root = nodes[0]
        while (1):
            root.visited = 1
            min_distance = float("inf")
            next_root = None
            if self.is_neighbor(root.word, end):
                return root.distance + 1
            for node in nodes:
                if not node.visited:
                    if self.is_neighbor(root.word, node.word):
                        node.distance = min(node.distance, root.distance+1)
                    if node.distance < min_distance:
                        next_root = node
                        min_distance = node.distance
            if not next_root:
                return 0
            root = next_root

print Solution().ladderLength("hit", "cog", ["hot","dot","dog","lot","log"])