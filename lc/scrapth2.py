

class a(object):
    def __init__(self):
        a.c = 0
        a.x = 1


A = a(c = 3, x = 1)

exit(0)

def generate_power_func(n):
    print "id(n): %X" % id(n)
    def nth_power(x):
        return x**n
    print "id(nth_power): %X" % id(nth_power)
    return nth_power

def generate_power_func1(n):
    print "id(n): %X" % id(n)


r4 = generate_power_func(4)
r41 = generate_power_func(4)
r42 = generate_power_func(5)
print r4(3)