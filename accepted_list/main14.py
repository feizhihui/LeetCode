# encoding=utf-8
'''
Longest Common Prefix:
Write a function to find the longest common prefix string amongst an array of strings.
'''


class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ''
        line = strs[0]
        for i, c in enumerate(line):
            for s in strs[1:]:
                if i >= len(s) or c != s[i]:
                    return line[:i]

        return line


if __name__ == '__main__':
    s = Solution()
    line = s.longestCommonPrefix(["aa", "a"])
    print(line)
