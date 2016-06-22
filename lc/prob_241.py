class Solution:
    # @param {string} input
    # @return {integer[]}
    def diffWaysToCompute(self, input):
        self.results = []
        last_idx = -1
        self.nums = []
        self.ops = []
        for idx in xrange(0, len(input)):
            if input[idx] in ('+-*'):
                self.nums.append(int(input[last_idx+1:idx]))
                self.ops.append(input[idx])
                last_idx = idx
        self.nums.append(int(input[last_idx+1:]))
        if len(self.nums) == 0:
            return None
        elif len(self.nums) == 1:
            return [self.nums[0]]
        self.recurs(self.nums, self.ops, -1)
        return self.results

    def recurs(self, nums, ops, primary):
        if len(ops) == 1:
            if ops[0] == '+':
                self.results.append(nums[0] + nums[1])
            elif ops[0] == '-':
                self.results.append(nums[0] - nums[1])
            else:
                self.results.append(nums[0] * nums[1])
            return
        for idx, op in enumerate(ops):
            if idx >= primary - 1:
                if op == '+':
                    self.recurs(nums[:idx] + [nums[idx] + nums[idx+1]] + nums[idx+2:], ops[:idx] + ops[idx+1:], idx)
                elif op == '-':
                    self.recurs(nums[:idx] + [nums[idx] - nums[idx+1]] + nums[idx+2:], ops[:idx] + ops[idx+1:], idx)
                else:
                    self.recurs(nums[:idx] + [nums[idx] * nums[idx+1]] + nums[idx+2:], ops[:idx] + ops[idx+1:], idx)

print Solution().diffWaysToCompute("2*3-4*5")