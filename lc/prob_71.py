class Solution:
    # @param {string} path
    # @return {string}
    def simplifyPath(self, path):
        path = path.strip()
        abs_path = path.startswith('/')
        levels = []
        for level in path.split('/'):
            if level:
                if level == '.':
                    pass
                elif level == '..':
                    if abs_path and not levels:
                        pass
                    elif levels and levels[-1] != '..':
                        levels.pop()
                    else:
                        levels.append('..')
                else:
                    levels.append(level)
        return ('/' if abs_path else '') + '/'.join(levels)

print Solution().simplifyPath('/../sds/../s///')