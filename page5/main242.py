# encoding=utf-8

from collections import defaultdict


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        dic = defaultdict(int)
        for c in s:
            dic[c] = dic[c] + 1
        for c in t:
            if c not in dic:
                return False
            dic[c] = dic[c] - 1
        for (v, c) in dic.items():
            if c != 0:
                return False
        return True


if __name__ == '__main__':
    sl = Solution()
    a = sl.isAnagram('abcdeab', 'adeabbc')
    print(a)
