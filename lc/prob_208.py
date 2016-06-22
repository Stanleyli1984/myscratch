class TrieNode:
    # Initialize your data structure here.
    def __init__(self):
        self.is_key = False
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()

    # @param {string} word
    # @return {void}
    # Inserts a word into the trie.
    def insert(self, word):
        ptr = self.root
        for char in word:
            if char not in ptr.children:
                ptr.children[char] = TrieNode()
            ptr = ptr.children[char]
        ptr.is_key = True

    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the trie.
    def search(self, word):
        ptr = self.root
        for char in word:
            if char in ptr.children:
                ptr = ptr.children[char]
            else:
                return False
        return ptr.is_key

    # @param {string} prefix
    # @return {boolean}
    # Returns if there is any word in the trie
    # that starts with the given prefix.
    def startsWith(self, prefix):
        ptr = self.root
        for char in prefix:
            if char in ptr.children:
                ptr = ptr.children[char]
            else:
                return False
        return True

# Your Trie object will be instantiated and called as such:
# trie = Trie()
# trie.insert("somestring")
# trie.search("key")