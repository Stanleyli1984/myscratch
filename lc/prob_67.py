class Solution:
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):
        result = ""
        carrier = 0
        for i in xrange(0, max(len(a), len(b))):
            if i >= len(a):
                add1 = 0
            else:
                add1 = a[len(a) - 1 -i]

            if i >= len(b):
                add2 = 0
            else:
                add2 = b[len(b) - 1 -i]
            result = str((int(add1) + int(add2) + carrier) % 2) + result
            carrier = (int(add1) + int(add2) + carrier) / 2
        if carrier:
            result = '1' + result
        return result

print Solution().addBinary("1", "1")