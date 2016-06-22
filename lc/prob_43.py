class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if '0' in [num1,   num2]:
            return '0'

        num1s = [ord(x) - ord('0') for x in reversed(num1)]
        num2s = [ord(x) - ord('0') for x in reversed(num2)]
        result_list = [0] * (len(num1s) + len(num2s) + 1)

        for xi, x in enumerate(num2s + [0]):
            carry = 0
            r_carry = 0
            for yi, y in enumerate(num1s + [0]):
                carry, item = divmod(carry + x * y, 10)
                r_carry, r_item = divmod(item + r_carry + result_list[xi+yi], 10)
                result_list[xi+yi] = r_item

        first_non_zero = False
        final_result = []
        for x in reversed(result_list):
            if first_non_zero or x:
                first_non_zero = True
                final_result.append(x)

        return ''.join((str(x) for x in final_result))

print Solution().multiply('99', '99')