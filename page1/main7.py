# encoding=utf-8
'''
Reverse Integer
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:
Input: 123
Output:  321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
'''


class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            ans = int('-' + str(-x)[::-1])
        else:
            ans = int(str(x)[::-1])
        if ans <= (1 << 31) - 1 and ans >= -(1 << 31):
            return ans
        else:
            return 0


if __name__ == '__main__':
    s = Solution()
    print(s.reverse(1534236469))
