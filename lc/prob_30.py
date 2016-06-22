# from collections import deque
#
# class Solution(object):
#     def findSubstring(self, s, words):
#         """
#         :type s: str
#         :type words: List[str]
#         :rtype: List[int]
#         """
#
#         words_dict = {}
#         results = []
#         for word in words:
#             words_dict[word] = words_dict.get(word, 0) + 1
#         step = len(words[0])
#         dict_len = len(words[0]) * len(words)
#         for shift in xrange(step):
#             bad_word_idx = -1
#             new_word_dict = {}
#             if shift + dict_len > len(s):
#                 continue
#             for i in xrange(len(words)):
#                 new_word = s[shift + i * step: shift + i * step + step]
#                 if new_word not in words_dict:
#                     bad_word_idx = i
#                 else:
#                     new_word_dict.setdefault(new_word, deque()).append(i)
#                     if len(new_word_dict[new_word]) > words_dict[new_word]:
#                         old_idx = new_word_dict[new_word].popleft()
#                         bad_word_idx = max(bad_word_idx, old_idx)
#             if bad_word_idx == -1:
#                 results.append(shift)
#             for idx in xrange(1, len(s)/len(words[0])-len(words) + 1):
#                 old_word = s[shift + idx * step - step: shift + idx * step]
#                 new_word = s[shift + idx * step + dict_len - step: shift + idx * step + dict_len]
#                 if old_word in new_word_dict and new_word_dict[old_word]:
#                     new_word_dict[old_word].popleft()
#                 if new_word not in words_dict:
#                     bad_word_idx = idx + len(words) - 1
#                 else:
#                     new_word_dict.setdefault(new_word, deque()).append(idx + len(words) - 1)
#                     if len(new_word_dict[new_word]) > words_dict[new_word] or len(new_word_dict[old_word]) < words_dict[old_word]:
#                         bad_word_idx = max(bad_word_idx, idx + len(words) - 1)
#                     else:
#                         if bad_word_idx < idx:
#                             results.append(idx*step + shift)
#         return results
#
# print Solution().findSubstring("aaa", ["a","b"])


class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        words_dict = {}
        results = []
        word_sum = 0
        for word in words:
            words_dict[word] = words_dict.get(word, 0) + 1
            word_sum += reduce(lambda x,y:x+y, map(ord, word))
        step = len(words[0])
        dict_len = len(words[0]) * len(words)
        for shift in xrange(step):
            count = 0
            new_sum = 0
            new_word_dict = {}
            if shift + dict_len > len(s):
                continue
            for i in xrange(len(words)):
                new_word = s[shift + i * step: shift + i * step + step]
                if new_word not in words_dict:
                    pass
                else:
                    new_word_dict[new_word] = new_word_dict.get(new_word, 0) + 1
                    count += 1
                    new_sum += reduce(lambda x,y:x+y, map(ord, new_word))
            if count == len(words) and new_word_dict == words_dict:
                results.append(shift)
            for idx in xrange(0, len(s)/len(words[0])-len(words)):
                old_word = s[shift + idx * step: shift + idx * step + step]
                new_word = s[shift + idx * step + dict_len: shift + idx * step + dict_len + step]
                if old_word in new_word_dict and new_word_dict[old_word]:
                    count -= 1
                    new_sum -= reduce(lambda x,y:x+y, map(ord, old_word))
                    new_word_dict[old_word] -= 1
                if new_word not in words_dict:
                    pass
                else:
                    count += 1
                    new_sum += reduce(lambda x,y:x+y, map(ord, new_word))
                    new_word_dict[new_word] = new_word_dict.get(new_word, 0) + 1
                    if count == len(words) and new_sum == word_sum and new_word_dict == words_dict:
                        results.append(idx*step + shift + step)
        return results

print Solution().findSubstring("barfoothefoobarman", ["foo","bar"])
