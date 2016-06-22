__author__ = 'zhongqil'

import itertools
def strider5(p, n):
    result = [ [ ] for x in itertools.repeat(0, n) ]
    resiter = itertools.cycle(result)
    for item, sublist in itertools.izip(p, resiter):
        print item, sublist
        sublist.append(item)
    print "Result", result
    return result


strider5(range(20), 3)
