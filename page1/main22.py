# encoding=utf-8

'''
Generate Parentheses:
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
For example, given n = 3, a solution set is:
[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
'''


class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.res = []
        ans = ['' for _ in range(2 * n)]
        self.dfs(ans, 0, 0, n)
        return self.res

    def dfs(self, qlist, lnum, rnum, total):
        if lnum == rnum == total:
            self.res.append(''.join(qlist))
            return
        if lnum > total or rnum > total:
            return
        if lnum > rnum:
            qlist[lnum + rnum] = '('
            self.dfs(qlist, lnum + 1, rnum, total)
            qlist[lnum + rnum] = ')'
            self.dfs(qlist, lnum, rnum + 1, total)
        else:
            qlist[lnum + rnum] = '('
            self.dfs(qlist, lnum + 1, rnum, total)


if __name__ == '__main__':
    s = Solution()
    s.generateParenthesis(3)
    print(s.res)
