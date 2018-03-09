# encoding=utf-8



'''
N-Queue
'''

from copy import deepcopy


class Solution:
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.board = [['.' for row in range(n)] for col in range(n)]
        self.result = []
        self.n = n
        self.dfs(0)
        result = []
        for bo in self.result:
            ans = [''.join(l) for l in bo]
            result.append(ans)
        return result

    def dfs(self, row):
        if row == self.n:
            self.result.append(deepcopy(self.board))
            return

        for i in range(self.n):
            if self.display(row, i):
                self.board[row][i] = 'Q'
                self.dfs(row + 1)
                self.board[row][i] = '.'

    def display(self, x, y):
        # x row
        for col in range(self.n):
            if self.board[x][col] != '.':
                return False
        # x col
        for row in range(self.n):
            if self.board[row][y] != '.':
                return False
        # left up
        m, n = x, y
        while m >= 0 and n >= 0:
            if self.board[m][n] != '.':
                return False
            m -= 1
            n -= 1
        # left down
        m, n = x, y
        while m < self.n and n >= 0:
            if self.board[m][n] != '.':
                return False
            m += 1
            n -= 1
        m, n = x, y
        # right up
        while m >= 0 and n < self.n:
            if self.board[m][n] != '.':
                return False
            m -= 1
            n += 1
        # right down
        m, n = x, y
        while m < self.n and n < self.n:
            if self.board[m][n] != '.':
                return False
            m += 1
            n += 1

        return True


if __name__ == '__main__':
    s = Solution()
    result = s.solveNQueens(4)
    print(result)
    print(len(result))
