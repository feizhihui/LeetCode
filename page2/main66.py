# encoding=utf-8

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        p = 1
        for i in reversed(range(len(digits))):
            digits[i] = digits[i] + p
            p = digits[i] // 10
            digits[i] = digits[i] % 10
            if p == 0:
                break
        if p != 0:
            digits = [p] + digits
        return digits


if __name__ == '__main__':
    sl = Solution()
    arr = sl.plusOne([2, 1])
    print(arr)
