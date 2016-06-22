__author__ = 'zhongqil'
from ctypes import *
class BLOCK(Structure):
    _fields_ = ("x", c_float), ("buffer",c_char * 32)

class BlockUsage(Structure):
    #_fields_ = [('block_array', BLOCK * 64)]
    _fields_ = ("id", c_uint64), ("usage", c_uint64)

#s1 = c_int64 * 64
#s2 = (c_char * 32) * 64

class getUsage(type):
    def __init__(self):
        pass

    def get_usage(self):
        result = {}
        BlockUsageType = BlockUsage * 64
        #pyarr = xrange(64)
        #s1 = (c_int64 * len(pyarr))(*pyarr)
        #s1._fields_[0] = (0.1, "cc")
        all_usages = BlockUsageType()
        dll = CDLL('C:/work/testCtype.dll')
        dll.func(all_usages)
        for usage in all_usages:
            result[usage.id] = usage.usage
        print "finished successfully"
        return result
        #print s1.buffer
        #print s1.x