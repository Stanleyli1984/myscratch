# class Solution:
#     # @param s, a string
#     # @param wordDict, a set<string>
#     # @return a boolean
#     def wordBreak(self, s, wordDict):
#         if not s or not wordDict:
#             return False
#         self.s = s
#         self.s_len = len(s)
#         self.dict_set = set(wordDict)
#         lens = [len(x)for x in self.dict_set]
#         self.min_word_len = min(lens)
#         self.max_word_len = max(lens)
#         return self.recurs(0)
#
#     def recurs(self, idx):
#         for idx1 in xrange(self.min_word_len, self.max_word_len + 1):
#             if idx + idx1 > self.s_len:
#                 return False
#             word = self.s[idx: idx + idx1]
#             if idx + idx1 == self.s_len:
#                 if word in self.dict_set:
#                     return True
#                 else:
#                     return False
#             else:
#                 if word in self.dict_set and self.recurs(idx + idx1):
#                     return True
#         return False


# class Solution:
#     # @param s, a string
#     # @param wordDict, a set<string>
#     # @return a boolean
#     def wordBreak(self, s, wordDict):
#         if not s or not wordDict:
#             return False
#         self.s_len = len(s)
#
#         stats = [True] + [False] * self.s_len
#         while any(stats):
#             new_stats = [False] * (self.s_len + 1)
#             for idx, stat in enumerate(stats):
#                 if stat:
#                     now_s = s[idx:]
#                     for word in wordDict:
#                         if now_s.startswith(word):
#                             if idx + len(word) == self.s_len:
#                                 return True
#                             else:
#                                 new_stats[idx + len(word)] = True
#             stats = new_stats
#         return False

class Solution:
    # @param s, a string
    # @param wordDict, a set<string>
    # @return a boolean
    def wordBreak(self, s, wordDict):
        if not s or not wordDict:
            return False
        self.s_len = len(s)
        self.dict_set = set(wordDict)

        stats = [True] + [False] * self.s_len
        for idx in xrange(1, self.s_len + 1):
            if not any(stats):
                return False
            for idx1 in xrange(0, idx):
                if stats[idx1]:
                    if s[idx1:idx] in self.dict_set:
                        if idx == self.s_len:
                            return True
                        stats[idx] = True
                        break
        return False

print Solution().wordBreak("applepeach", ["pear","apple","peach"])