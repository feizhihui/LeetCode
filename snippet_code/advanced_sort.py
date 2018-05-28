# encoding=utf-8



"""
class LargerNumKey(str):
    def __lt__(x, y):
        return x+y > y+x

class Solution:
    def largestNumber(self, nums):
        largest_num = ''.join(sorted(map(str, nums), key=LargerNumKey))
        return '0' if largest_num[0] == '0' else largest_num
"""

from functools import cmp_to_key


class Solution:
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        arr = list(map(str, nums))
        cmp2key = cmp_to_key(lambda x, y: int(y + x) - int(x + y))
        large_num = ''.join(sorted(arr, key=cmp2key))
        return '0' if large_num[0] == '0' else large_num


if __name__ == '__main__':
    sol = Solution()
    arr = [0, 0]

    arr = sol.largestNumber(arr)
    print(arr)
