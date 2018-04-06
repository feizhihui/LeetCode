# encoding=utf-8

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        pool = set()
        pool.add(n)
        while True:
            total = 0
            while n > 0:
                total += (n % 10) ** 2
                n //= 10
            if total == 1:
                return True
            print(total)
            n = total
            if n in pool:
                return False
            pool.add(n)



if __name__ == '__main__':
    sl = Solution()
    sl.isHappy(119)
