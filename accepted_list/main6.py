# encoding=utf-8
'''
ZigZag Conversion
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
'''


class Solution:
    class Solution(object):
        def convert(self, s, numRows):
            """
            :type s: str
            :type numRows: int
            :rtype: str
            """
            if numRows == 1 or numRows >= len(s):
                return s

            L = [''] * numRows
            index, step = 0, 1

            for c in s:
                L[index] += c
                if index == 0:  # arrive bottom
                    step = 1
                elif index == numRows - 1:  # arrive top
                    step = -1
                index += step

            return ''.join(L)


if __name__ == '__main__':
    s = Solution()
    ans = s.convert('ABC', 2)  # PAYPALISHIRING
    print(ans)
