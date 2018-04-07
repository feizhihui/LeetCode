# encoding=utf-8

class Solution(object):
    # basic method
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        for i in range(2, n):
            j = 2
            while j * j <= i:
                if i % j == 0:
                    break
                j += 1
            if j * j > i:
                count += 1

        return count


if __name__ == '__main__':
    sl = Solution()
    a = sl.countPrimes(999983)
    print(a)
