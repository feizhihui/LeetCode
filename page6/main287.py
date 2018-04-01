# encoding=utf-8

class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums) - 1
        total = sum(nums)
        return total - n * (n + 1) // 2


if __name__ == '__main__':
    sl = Solution()
    ans = sl.findDuplicate([1, 1])
    print(ans)
