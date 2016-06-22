class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        n = numerator
        d = denominator
        neg_sign = False
        if n < 0:
            neg_sign = True
            n = -n
        if d < 0:
            neg_sign = not neg_sign
            d = -d
        q_l, remain = divmod(n, d)
        if remain == 0:
            if q_l == 0:
                return '0'
            if neg_sign:
                return '-' + str(q_l)
            else:
                return str(q_l)
        pos = 0
        table = {}
        string = []
        while True:
            table[remain] = pos
            remain *= 10
            q_r, remain = divmod(remain, d)
            string.append(q_r)
            if remain == 0:
                break
            if remain in table:
                string.insert(table[remain], '(')
                string.append(')')
                break
            pos += 1
        if neg_sign:
            return '-' + str(q_l) + '.' + ''.join([str(x) for x in string])
        else:
            return str(q_l) + '.' + ''.join([str(x) for x in string])

print Solution().fractionToDecimal(-2147483648, 1)