# encoding=utf-8

class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        total = 0
        for c in s:
            total = total * 26 + ord(c) - 64
        return total


if __name__ == '__main__':
    pass
