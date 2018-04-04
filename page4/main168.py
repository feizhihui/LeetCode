# encoding=utf-8

class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        ans = []
        radix = 26
        while n > 0:
            n = n - 1
            ans.append(chr(n % radix + 65))
            n = n // 26
        return ''.join(ans[::-1])


if __name__ == '__main__':
    sl = Solution()
    a = sl.convertToTitle(300)
    print(a)
