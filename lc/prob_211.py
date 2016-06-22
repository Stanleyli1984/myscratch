class WordDictionary:
    # initialize your data structure here.
    def __init__(self):
       self.trie = {}

    # @param {string} word
    # @return {void}
    # Adds a word into the data structure.
    def addWord(self, word):
        trie_dict = self.trie
        for char in word:
            trie_dict = trie_dict.setdefault(char, {})
        trie_dict['#'] = 0

    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the data structure. A word could
    # contain the dot character '.' to represent any one letter.
    def search(self, word):
        possible_dicts = [self.trie]
        for char in word:
            new_possible_dicts = []
            if char == '.':
                for c_dict in possible_dicts:
                    new_possible_dicts.extend([v for v in c_dict.values() if isinstance(v, dict)])
            else:
                for c_dict in possible_dicts:
                    if char in c_dict:
                        new_possible_dicts.append(c_dict[char])
            possible_dicts = new_possible_dicts
            if not possible_dicts:
                return  False
        for c_dict in possible_dicts:
            if '#' in c_dict:
                return True
        return False



# Your WordDictionary object will be instantiated and called as such:
wordDictionary = WordDictionary()
wordDictionary.addWord("word")
wordDictionary.addWord("word1")
print wordDictionary.search("w.r.1")