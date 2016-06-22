class Solution:
    # @param board, a list of lists of 1 length string
    # @param word, a string
    # @return a boolean

    def __init__(self):
        self.statuses = []
        self.found = False

    def exist(self, board, word):
        self.statuses = [[0] * len(board[0]) for _ in xrange(len(board))]
        for x in xrange(len(board)):
            for y in xrange(len(board[0])):
                if word[0] == board[x][y]:
                    if len(word) == 1:
                        return True
                    else:
                        self.statuses[x][y] = 1
                        if (self.recursive(x, y, 1,  word, board)):
                            return True
                        self.statuses[x][y] = 0
        return False

    def recursive(self, orig_x, orig_y, pos, word, board):
        for x, y in ((orig_x + 1, orig_y),(orig_x, orig_y+1),(orig_x - 1, orig_y),(orig_x, orig_y-1)):
            if 0 <= x < len(board) and 0 <= y < len(board[0]) and self.statuses[x][y] == 0:
                if (board[x][y] == word[pos]):
                    if pos == len(word) - 1:
                        return True
                    else:
                        self.statuses[x][y] = 1
                        if (self.recursive(x, y, pos+1,word,board)):
                            return True
                        self.statuses[x][y] = 0
        return False

print Solution().exist(["ABCE","SFCS","ADEE"], "ABCB")

