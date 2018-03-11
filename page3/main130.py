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
        self.n = len(board)
        self.m = len(board[0])
        coor_list = []
        for i in range(self.n):
            if board[i][0] == 'O':
                coor_list.append((i, 0))
            if board[i][self.m - 1] == 'O':
                coor_list.append((i, self.m - 1))

        for j in range(self.m):
            if board[0][j] == 'O':
                coor_list.append((0, j))
            if board[self.n - 1][j] == 'O':
                coor_list.append((self.n - 1, j))

        self.bfs(coor_list, board)

        for i in range(self.n):
            for j in range(self.m):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'S':
                    board[i][j] = 'O'

    def bfs(self, coor_list, board):  # calculate how many Non Unicom region
        """
        :param x:
        :param y:
        :return:
        """
        around = True  # around by X
        while len(coor_list) > 0:
            neighbors = []
            for (i, j) in coor_list:
                board[i][j] = 'S'
                if i - 1 < 0 or i + 1 >= self.n or j - 1 < 0 or j + 1 >= self.m:
                    around = False
                if i - 1 >= 0 and board[i - 1][j] == 'O':
                    neighbors.append((i - 1, j))
                if i + 1 < self.n and board[i + 1][j] == 'O':
                    neighbors.append((i + 1, j))
                if j - 1 >= 0 and board[i][j - 1] == 'O':
                    neighbors.append((i, j - 1))
                if j + 1 < self.m and board[i][j + 1] == 'O':
                    neighbors.append((i, j + 1))
            coor_list = neighbors


if __name__ == '__main__':
    s = Solution()
    board = [['O']]
    s.solve(board)

    print(board)
