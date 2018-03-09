# encoding=utf-8
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = '1'
        for i in range(n - 1):
            count = 1
            ans = []
            for index in range(1, len(s)):
                if s[index] == s[index - 1]:
                    count += 1
                else:
                    ans.append(str(count))
                    ans.append(s[index - 1])
                    count = 1
            ans.append(str(count))
            ans.append(s[-1])
            s = ''.join(ans)
        return s


if __name__ == '__main__':
    s = Solution()
    print(s.countAndSay(5))
