# encoding=utf-8

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        s = bin(n)[2:]
        return len([c for c in s if c == '1'])


if __name__ == '__main__':
    sl = Solution()
    ans = sl.hammingWeight(2)
    print(ans)
