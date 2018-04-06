# encoding=utf-8

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if len(nums) <= 2:
            return max(nums)
        if len(nums) == 3:
            return max(nums[1], nums[0] + nums[2])
        ret = [0] * len(nums)
        ret[:2] = nums[:2]
        ret[2] = nums[0] + nums[2]
        for i in range(3, len(nums)):
            ret[i] = nums[i] + max(ret[i - 2], ret[i - 3])
        return max(ret[-2:])


if __name__ == '__main__':
    sl = Solution()
    a = sl.rob([1, 1, 2, 1])
    print(a)
