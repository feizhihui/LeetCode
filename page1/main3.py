# encoding=utf-8


'''
Longest Substring Without Repeating Characters
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.
Given "bbbbb", the answer is "b", with the length of 1.
Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring,
"pwke" is a subsequence and not a substring.
'''


class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == "":
            return 0
        d = {}
        max_lens = 0
        i = j = 0
        for j, c in enumerate(s):
            if c in d and i <= d[c]:
                max_lens = j - i if max_lens < j - i else max_lens
                i = d[c] + 1
            d[c] = j
        else:
            j += 1
        return j - i if max_lens < j - i else max_lens


if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLongestSubstring(""))
