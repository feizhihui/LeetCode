# encoding=utf-8
"""
Isomorphic Strings
"""


class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        n = len(s)
        d = dict()
        for i in range(n):
            c1 = s[i]
            c2 = t[i]
            if c1 in d and d[c1] != c2:
                return False
            d[c1] = c2
        return len(set(s)) == len(set(t))


if __name__ == '__main__':
    sl = Solution()
    ans = sl.isIsomorphic('aa', 'ab')
    print(ans)
