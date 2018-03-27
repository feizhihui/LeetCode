# encoding=utf-8

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        for num in nums:
            ans ^= num
        return ans


if __name__ == '__main__':
    sl = Solution()
    ans = sl.singleNumber([-2, -3, -6, -3, -2, -5, -5])
    print(ans)
