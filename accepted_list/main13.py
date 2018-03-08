# encoding=utf-8

'''
Roman to Integer:
Given a roman numeral, convert it to an integer.
Input is guaranteed to be within the range from 1 to 3999.
'''

M = {"M": 1000, "MM": 2000, "MMM": 3000}  # 100*(1~3)
C = {"C": 100, "CC": 200, "CCC": 300, "CD": 400, "D": 500, "DC": 600, "DCC": 700, "DCCC": 800, "CM": 900}  # 100*(1~9)
X = {"X": 10, "XX": 20, "XXX": 30, "XL": 40, "L": 50, "LX": 60, "LXX": 70, "LXXX": 80, "XC": 90}  # 10*(1~9)
I = {"I": 1, "II": 2, "III": 3, "IV": 4, "V": 5, "VI": 6, "VII": 7, "VIII": 8, "IX": 9}  # 1~9


class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {}
        d.update(M)
        d.update(C)
        d.update(X)
        d.update(I)

        a = list(d.items())
        a.sort(key=lambda x: -x[1])  # inplace
        sum = 0
        while s != '':
            for x, num in a:
                if s.startswith(x):
                    sum += num
                    s = s[len(x):]
                    break
        return sum



if __name__ == '__main__':
    s = Solution()
    print(s.romanToInt('XLIV'))
