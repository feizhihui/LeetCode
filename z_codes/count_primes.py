# encoding=utf-8
import time


class Solution(object):
    # #  time about 10.60s
    # def countPrimes(self, n):
    #     """
    #     :type n: int
    #     :rtype: int
    #     """
    #     count = 0
    #     for i in range(2, n):
    #         j = 2
    #         while j * j <= i:
    #             if i % j == 0:
    #                 break
    #             j += 1
    #         if j * j > i:
    #             count += 1
    #     return count

    # print-table method  time about 0.48s
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0
        a = [True] * n
        a[0] = a[1] = False
        for i in range(2, n):
            if a[i]:
                j = i
                while i * j < n:
                    a[i * j] = False
                    j += 1
        return sum(a)


if __name__ == '__main__':
    tts = time.time()
    sl = Solution()
    a = sl.countPrimes(999983)
    print(a)
    tte = time.time()
    print(tte - tts)
