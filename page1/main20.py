# encoding=utf-8

'''
Valid Parentheses:
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
'''


class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        d = {'[': ']', '{': '}', '(': ')'}
        stack = []
        for i, c in enumerate(s):
            if c in {'{', '[', '('}:
                stack.append(c)
            elif c in {'}', ']', ')'}:
                if len(stack) == 0:
                    return False
                v = stack.pop()
                if d[v] != c:
                    return False
        return len(stack) == 0


if __name__ == '__main__':
    s = Solution()
    print(s.isValid('[]'))
