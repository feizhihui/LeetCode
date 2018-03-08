# encoding=utf-8
'''
 Longest Palindromic Substring

Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
Example:
Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example:
Input: "cbbd"
Output: "bb"
'''


class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        m = len(s)
        maxlens = 0
        ans = ''
        # odd palindromic
        for i in range(m):
            j = 0
            while i + j < m and i - j >= 0 and s[i + j] == s[i - j]:
                j += 1
            j -= 1
            if 2 * j + 1 > maxlens:
                maxlens = 2 * j + 1
                ans = s[i - j:i + j + 1]
        # even palindromic
        for i in range(m):
            j = 0
            while i + 1 + j < m and i - j >= 0 and s[i + 1 + j] == s[i - j]:
                j += 1
            if 2 * j > maxlens:
                maxlens = 2 * j
                ans = s[i - j + 1:i + j + 1]

        return ans


if __name__ == '__main__':
    s = Solution()
    h = s.longestPalindrome("a")
    print(h)
