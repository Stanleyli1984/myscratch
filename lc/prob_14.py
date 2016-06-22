class Solution:
    # @param {string[]} strs
    # @return {string}
    def longestCommonPrefix(self, strs):
        if not strs or len(strs[-1]) == 0:
            return ""
        common_part_idx = len(strs[-1])
        for string in reversed(strs):
            idx = 0
            while idx < min(len(string), common_part_idx):
                if string[idx] != strs[-1][idx]:
                    break
                idx += 1
            common_part_idx = idx
        return strs[-1][:common_part_idx]

print Solution().longestCommonPrefix(["abc", "abc", "abc"])