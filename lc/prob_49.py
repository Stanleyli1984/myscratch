class Solution:
    # @param {string[]} strs
    # @return {string[]}
    def anagrams(self, strs):
        result = []
        all_str_dicts = {}
        qualify_str_dicts = set()
        for string in strs:
            str_dict = tuple(sorted(string))
            if str_dict in all_str_dicts:
                qualify_str_dicts.add(str_dict)
                all_str_dicts[str_dict].append(string)
            else:
                all_str_dicts[str_dict] = [string]
        for str_dict in qualify_str_dicts:
            result.extend(all_str_dicts[str_dict])
        return result

print Solution().anagrams(['abd', 'bad', 'abc'])