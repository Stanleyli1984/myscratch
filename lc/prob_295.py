import heapq

class MedianFinder:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.min_array = []
        self.max_array = []

    def addNum(self, num):
        """
        Adds a num into the data structure.
        :type num: int
        :rtype: void
        """
        if not self.min_array and not self.max_array:
            self.min_array = [num]
        else:
            if num > self.min_array[0]:
                heapq.heappush(self.min_array, num)
            else:
                heapq.heappush(self.max_array, -num)

        if len(self.min_array) > len(self.max_array) + 1:
            heapq.heappush(self.max_array, -heapq.heappop(self.min_array))
        elif len(self.max_array) > len(self.min_array) + 1:
            heapq.heappush(self.min_array, -heapq.heappop(self.max_array))


    def findMedian(self):
        """
        Returns the median of current data stream
        :rtype: float
        """
        if len(self.min_array) ==  len(self.max_array):
            return (self.min_array[0] - self.max_array[0]) / 2.0
        else:
            return self.min_array[0] if len(self.min_array) > len(self.max_array) else -self.max_array[0]


# Your MedianFinder object will be instantiated and called as such:
mf = MedianFinder()
mf.addNum(2)
mf.addNum(1)
mf.addNum(1)
mf.addNum(2)
print mf.findMedian()