class Solution:
    # @param {character[][]} board
    # @param {string[]} words
    # @return {string[]}
    def findWords(self, board, words):
        self.board = board
        self.trie = {}
        x = len(board)
        y = len(board[0])
        self.total = x * y
        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                remaining = self.total
                next_batch = [((i, j), self.trie, set())]
                while next_batch:
                    new_batch = []
                    for pos, trie_hash, visited_nodes in next_batch:
                        char = self.board[pos[0]][pos[1]]
                        if char not in trie_hash:
                            trie_hash[char] = {}
                        for new_pos in ((pos[0], pos[1] + 1), (pos[0], pos[1] - 1), (pos[0] + 1, pos[1]), (pos[0] - 1, pos[1])):
                            if 0 <= new_pos[0] < x and 0 <= new_pos[1] < y and (new_pos not in visited_nodes):
                                new_batch.append((new_pos, trie_hash[char], visited_nodes|{new_pos}))
                    next_batch = new_batch
                    #remaining -= 1



        self.results = []
        for word in words:
            whole_word_in = True
            trie_dict = self.trie
            for char in word:
                if char in trie_dict:
                    trie_dict = trie_dict[char]
                else:
                    whole_word_in = False
            if whole_word_in:
                self.results.append(word)
        return self.results


#print Solution().findWords(["ab","cd"], ["aa","bc","cd","da","bd"])
print Solution().findWords(["bbaaba","bbabaa","bbbbbb","aaabaa","abaabb"], ["abbbababaa"])