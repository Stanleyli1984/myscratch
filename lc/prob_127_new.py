class Solution:
    # @param {string} beginWord
    # @param {string} endWord
    # @param {set<string>} wordDict
    # @return {integer}
    def ladderLength(self, beginWord, endWord, wordDict):
        if not wordDict:
            return 0
        letters = [chr(x) for x in xrange(ord('a'), ord('z') + 1)]

        current_word_sets = [{beginWord}, {endWord}]
        step = 1
        word_len = len(beginWord)
        working_idx = 0
        while current_word_sets[0] or current_word_sets[1]:
            step += 1
            new_word_set = set()
            for word in current_word_sets[working_idx]:
                for pos in xrange(word_len):
                    for char in letters:
                        c_word = word[:pos] + char + word[pos+1:]
                        #print c_word
                        if (working_idx == 0 and c_word == endWord) or (working_idx == 1 and c_word == beginWord):
                            return step
                        if c_word in current_word_sets[1-working_idx]:
                            return step
                        if c_word in wordDict:
                            wordDict.discard(c_word)
                            new_word_set.add(c_word)
            current_word_sets[working_idx] = new_word_set
            working_idx = 0 if (len(current_word_sets[0]) < len(current_word_sets[1])) else 1
            if len(current_word_sets[0]) == 0:
                working_idx = 1
            if len(current_word_sets[1]) == 0:
                working_idx = 0

        return 0

#print Solution().ladderLength("hot", "dog", {"hot","dog"})
#print Solution().ladderLength("aaa", "abc", {"aac"})
print Solution().ladderLength("hit", "cog", {"hot","dot","dog","lot","log"})