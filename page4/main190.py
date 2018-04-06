# encoding=utf-8

class Solution:
    def reverseBits(self, n):
        """
        :param n:
        :return integer:
        """
        s = bin(n)[2:].zfill(32)
        return int(s[::-1], 2)


if __name__ == '__main__':
    sl = Solution()
    n = sl.reverseBits(43261596)
    print(n)
