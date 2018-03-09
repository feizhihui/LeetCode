# encoding=utf-8

class Solution:
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """

        self.n = len(board)
        if self.n == 0:
            return board
        self.m = len(board[0])
        if self.m == 0:
            return board
        self.board = board
        self.occur = [[0 for _ in range(self.m)] for _ in range(self.n)]
        for i in range(self.n):
            for j in range(self.m):
                if self.board[i][j] == 'O':
                    self.dfs(i, j)
        return self.board

    def dfs(self, i, j):
        """
        :param x:
        :param y:
        :return:
        """
        if self.occur[i][j] == 1:
            return True
        self.occur[i][j] = 1

        if i - 1 < 0 or i + 1 >= self.n or j - 1 < 0 or j + 1 >= self.m:
            return False

        if i - 1 >= 0 and self.board[i - 1][j] == 'O':
            if not self.dfs(i - 1, j):
                return False
        if i + 1 < self.n and self.board[i + 1][j] == 'O':
            if not self.dfs(i + 1, j):
                return False
        if j - 1 >= 0 and self.board[i][j - 1] == 'O':
            if not self.dfs(i, j - 1):
                return False
        if j + 1 < self.m and self.board[i][j + 1] == 'O':
            if not self.dfs(i, j + 1):
                return False

        # around is wall
        self.board[i][j] = 'X'
        return True


if __name__ == '__main__':
    s = Solution()
    board = s.solve([['X', 'X', 'X', 'X'],
                     ['X', 'O', 'O', 'X'],
                     ['X', 'X', 'O', 'X'],
                     ['X', 'O', 'X', 'X'],
                     ['X', 'X', 'X', 'X'],
                     ['X', 'O', 'O', 'X'],
                     ['X', 'X', 'O', 'O'],
                     ['X', 'O', 'X', 'O']])
    # board = s.solve([])
    print(board)
