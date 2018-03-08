# encoding=utf-8

class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        sum = 0
        x_ = x
        while x_ > 0:
            sum = 10 * sum + x_ % 10
            x_ //= 10
        return sum == x


if __name__ == '__main__':
    s = Solution()
    print(s.isPalindrome(12321))
