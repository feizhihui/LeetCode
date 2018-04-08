# encoding=utf-8
class Solution:
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 1:
            return False
        while n > 1:
            if n % 2 != 0:
                return False
            n //= 2

        return True


if __name__ == '__main__':
    pass
