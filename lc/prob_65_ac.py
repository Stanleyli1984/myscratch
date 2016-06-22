import re

class Solution:
    # @param s, a string
    # @return a boolean
    def isNumber(self, s):
        s = s.strip()
        m = re.match(r'[\-\+]?(.*)', s)
        s = m.group(1)
        m = re.match(r'0[xX](.*)', s)
        if m: #hex
            s = m.group(1)
            m = re.match(r'[0-9A-Fa-f]+$', s)
            if m:
                return True
            else:
                return False
        else:
            m = re.match(r'(.*)[eE](.*)', s)
            if m:
                part1 = m.group(1)
                part2 = m.group(2)
                m = re.match(r'[\-\+]?(.*)', part2)
                part2 = m.group(1)
                if re.match(r'[0-9]+\.[0-9]+$|[0-9]+\.?$|\.[0-9]+$', part1) and re.match(r'[0-9]+$', part2):
                    return True
                else:
                    return False
            else:
                if (re.match(r'[0-9]+\.[0-9]+$|[0-9]+\.?$|\.[0-9]+$', s)):
                    return True
                else:
                    return False
