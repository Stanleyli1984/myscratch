class MinStack:
    # initialize your data structure here.
    def __init__(self):
        self.data = []
        self.aux_data = []

    # @param x, an integer
    # @return nothing
    def push(self, x):
        self.data.append(x)
        if not self.aux_data:
            self.aux_data = [x]
        else:
            self.aux_data.append(min(x, self.aux_data[-1]))

    # @return nothing
    def pop(self):
        if self.data:
            self.data.pop()
            self.aux_data.pop()

    # @return an integer
    def top(self):
        if self.data:
            return self.data[-1]

    # @return an integer
    def getMin(self):
        if self.aux_data:
            return self.aux_data[-1]
