# encoding=utf-8

class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        low, high = 0, len(s) - 1
        s = s.lower()
        while low < high:
            while low < high and not s[low].isalnum():
                low += 1
            while low < high and not s[high].isalnum():
                high -= 1
            if low >= high:
                break
            if s[low] != s[high]:
                return False
            low += 1
            high -= 1
        return True


if __name__ == '__main__':
    sl = Solution()
    ans = sl.isPalindrome("0P")
    print(ans)
