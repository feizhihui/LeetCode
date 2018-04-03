# encoding=utf-8
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a = int(a, 2)
        b = int(b, 2)
        return bin(a + b)[2:]


if __name__ == '__main__':
    sl = Solution()
    s = sl.addBinary('101', '11111')
    print(s)
