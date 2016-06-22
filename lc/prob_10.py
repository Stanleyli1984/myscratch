class Solution:
    # @return a boolean
    def isMatch(self, s, p):
        # Tokenize
        all_tokens = []
        for idx in xrange(len(p)):
            if p[idx] == '*':
                continue
            if idx != len(p) - 1 and p[idx + 1] == '*':
                all_tokens.append(['*', p[idx]])
            else:
                all_tokens.append([p[idx]])
        l_token = all_tokens[:len(all_tokens)/2]
        r_token = all_tokens[len(all_tokens)/2:][::-1]
        l_s = s
        r_s = s[::-1]
        str_len = len(s)
        l_status = r_status = cur_status = [1] + [0]*len(s)
        for t_idx in xrange(len(all_tokens)/2 + 1):
            for loop in ['l', 'r']:
                if loop == 'l':
                    tokens = l_token
                    string = l_s
                    cur_status = l_status
                else:
                    tokens = r_token
                    string = r_s
                    cur_status = r_status
                try:
                    token = tokens[t_idx]
                except:
                    continue
                else:
                    next_status = [0] * (str_len + 1)
                    if token[0] == '*':
                        for c_idx in xrange(str_len + 1):
                            if cur_status[c_idx] == 1:
                                next_status[c_idx] = 1
                                for n_idx in xrange(c_idx + 1, str_len + 1):
                                    if (string[n_idx - 1] == token[1] or token[1] == '.'):
                                        next_status[n_idx] = 1
                                    else:
                                        break
                    else:
                        for c_idx in xrange(str_len):
                            if (cur_status[c_idx] == 1 and (token[0] in [string[c_idx], '.'])):
                                next_status[c_idx + 1] = 1
                    if not any(next_status):
                        return False
                    cur_status = next_status
                    if loop == 'l':
                        l_status = cur_status
                    else:
                        r_status = cur_status
        return any(map(lambda x, y: x and y, l_status, reversed(r_status)))

print Solution().isMatch("aaa", ".a.*")