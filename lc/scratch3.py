__author__ = 'zhongqil'

def cmp_func(num1, num2):
    return cmp(str(num1), str(num2))

print sorted(xrange(1, 1001),  cmp = cmp_func)