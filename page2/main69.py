# encoding=utf-8
import math


class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        # return int(math.sqrt(x))

        low, high = 0, x

        while low <= high:
            mid = (low + high) // 2
            if mid ** 2 < x:
                low = mid + 1
            elif mid ** 2 > x:
                high = mid - 1
            else:
                return mid

        return int(high)


if __name__ == '__main__':
    sl = Solution()
    ans = sl.mySqrt(11)
    print(ans)
