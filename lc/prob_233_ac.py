# class Solution:
#     # @param {integer} n
#     # @return {integer}
#     def countDigitOne(self, n):
#         tmp_n = n
#         digits = 0
#         while (tmp_n):
#             tmp_n /= 10
#             digits += 1
#         return self.count_recur(n, digits, False)
#
#     def count_recur(self, n, digits, is_max):
#         if digits == 1:
#             return 1 if n >= 1 else 0
#         else:
#             #432
#             whole_int = pow(10,  (digits - 1)) # 100
#             highest_digit = n / whole_int # 4
#             remaining = n - whole_int * highest_digit #32
#             if is_max:
#                 return 9 * self.count_recur(whole_int - 1, digits - 1, True) + whole_int
#             else:
#                 if highest_digit > 1:
#                     return self.count_recur(whole_int - 1, digits - 1, True) * (highest_digit - 1) + \
#                            self.count_recur(remaining, digits - 1, False) + whole_int
#                 elif highest_digit == 1:
#                     return remaining + 1 + self.count_recur(whole_int - 1, digits - 1, True)
#                 else:
#                     return self.count_recur(remaining, digits - 1, False)
#
# print Solution().countDigitOne(13)
#
# class Solution:
#     # @param {integer} n
#     # @return {integer}
#     def countDigitOne(self, n):
#         tmp_n = n
#         digits = 0
#         while (tmp_n):
#             tmp_n /= 10
#             digits += 1
#         return self.count_recur(n, digits, False)
#
#     def count_recur(self, n, digits):
#         if digits == 1:
#             return 1 if n >= 1 else 0
#         #432
#         whole_int = pow(10,  (digits - 1)) # 100
#         highest_digit = n / whole_int # 4
#         remaining = n - whole_int * highest_digit #32
#         if highest_digit > 1:
#             return whole_int + self.count_recur(whole_int - 1, digits - 1) * (highest_digit - 1)
#         elif highest_digit == 1:
#             return remaining + 1 + self.count_recur(whole_int - 1, digits - 1)
#         else:
#             return self.count_recur(remaining, digits - 1)

class Solution:
    # @param {integer} n
    # @return {integer}
    def countDigitOne(self, n):
        remaining_n = n
        #n: 456
        total = 0
        passed_dig = 0
        if n <= 0:
            return 0
        while remaining_n:
            passed_dig += 1
            powed = pow(10, passed_dig - 1)
            low_part = n % (powed * 10)
            high_part = n / (powed * 10)
            total += high_part * powed
            if low_part >= 2 * powed:
                total += powed
            elif low_part >= powed:
                total += low_part - powed + 1
            else:
                pass
            remaining_n /=10
        return total

print Solution().countDigitOne(13)