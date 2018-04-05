# encoding=utf-8


class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        total = 0
        while n // 5 > 0:
            total += n // 5
            n = n // 5
        return total


if __name__ == '__main__':
    pass
