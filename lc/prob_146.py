from collections import OrderedDict

class LRUCache(OrderedDict):
    'Store items in the order the keys were last added'
    def __init__(self, capacity):
        self._capacity = capacity
        self._count = 0
        OrderedDict.__init__(self)

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if key in self:
            del self[key]
        else:
            if self._count >= self._capacity:
                self.popitem(self, False)
            else:
                self._count += 1
        OrderedDict.__setitem__(self, key, value)

    # @return an integer
    def get(self, key):
        if key in self:
            value = self[key]
            del self[key]
            OrderedDict.__setitem__(self, key, value)
            return value
        else:
            return -1

a = LRUCache(1)
a.set(2, 1)
a.get(2)
