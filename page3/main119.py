# encoding=utf-8
from copy import deepcopy


class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        numRows = rowIndex + 1
        ans = [0] * numRows
        ans[0] = 1
        for i in range(numRows):
            previous = deepcopy(ans)
            for j in range(1, i + 1):
                ans[j] = previous[j - 1] + previous[j]

        return ans


if __name__ == '__main__':
    sl = Solution()
    res = sl.getRow(5)
    print(res)
