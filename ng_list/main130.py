# encoding=utf-8
'''
Surrounded Regions:
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.
A region is captured by flipping all 'O's into 'X's in that surrounded region.
'''


class Solution:
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """

        if not any(board):
            return
        self.m = len(board[0])
        self.n = len(board)

        self.board = board
        self.occur = [[0 for _ in range(self.m)] for _ in range(self.n)]
        count = 0
        for i in range(self.n):
            for j in range(self.m):
                if self.board[i][j] == 'O' and self.occur[i][j] == 0:
                    self.bfs(i, j)
                    count += 1

    def bfs(self, i, j):  # calculate how many Non Unicom region
        """
        :param x:
        :param y:
        :return:
        """
        coor_list = [(i, j)]
        span = []
        around = True  # around by X
        while len(coor_list) > 0:
            span.extend(coor_list)
            neighbors = []
            for (i, j) in coor_list:
                self.occur[i][j] = 1

                if i - 1 < 0 or i + 1 >= self.n or j - 1 < 0 or j + 1 >= self.m:
                    around = False
                if i - 1 >= 0 and self.board[i - 1][j] == 'O' and self.occur[i - 1][j] == 0:
                    neighbors.append((i - 1, j))
                if i + 1 < self.n and self.board[i + 1][j] == 'O' and self.occur[i + 1][j] == 0:
                    neighbors.append((i + 1, j))
                if j - 1 >= 0 and self.board[i][j - 1] == 'O' and self.occur[i][j - 1] == 0:
                    neighbors.append((i, j - 1))
                if j + 1 < self.m and self.board[i][j + 1] == 'O' and self.occur[i][j + 1] == 0:
                    neighbors.append((i, j + 1))
            coor_list = neighbors
        if around:
            for (i, j) in span:
                self.board[i][j] = 'X'


if __name__ == '__main__':
    s = Solution()
    board = [['O']]
    s.solve(board)

    print(board)
