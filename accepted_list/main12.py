# encoding=utf-8
M = ["", "M", "MM", "MMM"]  # 100*(1~4)
C = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]  # 100*(1~9)
X = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]  # 10*(1~9)
I = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]  # 1~9


class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        return M[num // 1000] + C[(num % 1000) // 100] + X[(num % 100) // 10] + I[num % 10]


if __name__ == '__main__':
    s = Solution()
    print(s.intToRoman(399))
