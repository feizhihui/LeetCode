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
        i = j = 0
        max_length = 0
        while j < len(s):
            c = s[j]
            ix = s[i:j].find(c)
            if ix < 0:
                j += 1
            else:
                if j - i > max_length:  # if find
                    max_length = j - i
                i = ix + i + 1
        if j - i > max_length:
            max_length = j - i
        return max_length


if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLongestSubstring("abcabcbb"))
