# encoding=utf-8

class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        ans = [[0 for i in range(numRows)] for j in range(numRows)]
        for i in range(numRows):
            ans[i][0] = 1
            for j in range(1, i + 1):
                ans[i][j] = ans[i - 1][j - 1] + ans[i - 1][j]
        res = [[ans[j][i] for i in range(numRows) if ans[j][i] != 0] for j in range(numRows)]
        return res


if __name__ == '__main__':
    sl = Solution()
    res = sl.generate(5)
    print(res)
