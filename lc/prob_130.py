class Solution:
    # @param {character[][]} board
    # @return {void} Do not return anything, modify board in-place instead.
    def solve(self, board):
        remaining = set()
        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                if board[i][j] == 'O':
                    remaining.add((i, j))
        while remaining:
            point = remaining.pop()
            this_batch = {point}
            cur_batch = {point}
            while cur_batch:
                new_cur_batch = set()
                for cur_point in cur_batch:
                    for coord in ((cur_point[0], cur_point[1] + 1), (cur_point[0], cur_point[1] - 1),
                                  (cur_point[0] + 1, cur_point[1]), (cur_point[0] - 1, cur_point[1])):
                        if coord in remaining:
                            remaining.remove(coord)
                            this_batch.add(coord)
                            new_cur_batch.add(coord)
                cur_batch = new_cur_batch
            need_revise = True
            for point in this_batch:
                if point[0] == 0 or point[1] == 0 or point[0] == len(board) - 1 or point[1] == len(board[0]) - 1:
                    need_revise = False
                    break
            if need_revise:
                for point in this_batch:
                    board[point[0]][point[1]] = 'X'
        return board

print Solution().solve([['X', 'O', 'X'], ['X', 'O', 'X'], ['X', 'O', 'X']])