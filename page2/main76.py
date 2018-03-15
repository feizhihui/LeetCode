# encoding=utf-8
from collections import deque

"""
S = "ADOBECODEBANC"
T = "ABC"
Minimum window is "BANC".

Note: Not Accepted!
"""


class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        tnum = {}
        pointer = deque()
        count = len(t)
        for c in t:
            tnum[c] = tnum.get(c, 0) + 1
        minlen = len(s) + 1
        best_j = -1
        for i, c in enumerate(s):
            # 遇到重复元素
            if count > 0 and c in tnum and tnum[c] == 0:
                for ix in pointer:
                    if s[ix] == c:
                        break
                pointer.remove(ix)
                pointer.append(i)
                continue

            # 找到未满足的目标元素
            if c in tnum and tnum[c] > 0:
                tnum[c] -= 1
                pointer.append(i)
                count -= 1

            # 目标元素查找完毕
            if count == 0:
                first_ix = pointer.popleft()
                if i - first_ix + 1 < minlen:
                    minlen = i - first_ix + 1
                    best_j = i
                # delete first element in queue
                count += 1
                e = s[first_ix]
                tnum[e] += 1
        return s[best_j - minlen + 1:best_j + 1]


if __name__ == '__main__':
    s = Solution()
    print(s.minWindow("ADOBECODEBANC", "ABC"))  # ADOBECODEBANC
    # print(s.minWindow("acbbaca", "aba"))  # ADOBECODEBANC
