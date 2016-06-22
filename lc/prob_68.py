class Solution:
    # @param {string[]} words
    # @param {integer} maxWidth
    # @return {string[]}
    def fullJustify(self, words, maxWidth):
        start_idx = 0
        results = []
        while True:
            result = []
            char_cnt_w_space = len(words[start_idx])
            end_idx = None
            for idx in xrange(start_idx + 1, len(words)):
                char_cnt_w_space += (1 + len(words[idx]))
                if char_cnt_w_space > maxWidth:
                    end_idx = idx - 1
                    break
            if end_idx is None:
                end_idx = len(words) - 1
            if end_idx == len(words) - 1:
                for idx in xrange(start_idx, len(words)):
                    result.append(words[idx])
                    if idx != end_idx:
                        result.append(' ')
                    else:
                        result.append(' ' * (maxWidth - sum(len(x) for x in result)))
                results.append(''.join(result))
                break
            else:
                spaces_len = maxWidth - sum(len(words[x]) for x in xrange(start_idx, end_idx + 1))
                gaps = 1 if (start_idx == end_idx) else end_idx - start_idx
                d, m = divmod(spaces_len, gaps)
                space_lens = [d] * gaps
                for i in xrange(m):
                    space_lens[i] += 1
                for i, idx in enumerate(xrange(start_idx, end_idx+1)):
                    result.append(words[idx])
                    if idx == start_idx or idx != end_idx:
                        result.append(' ' * space_lens[i])
                start_idx = end_idx + 1
                results.append(''.join(result))
        return results

print Solution().fullJustify(["justification.1"], 16)