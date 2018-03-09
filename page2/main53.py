# encoding=utf-8

'''
Maximum Subarray:
Find the contiguous subarray within an array (containing at least one number) which has the largest sum.
For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
the contiguous subarray [4,-1,2,1] has the largest sum = 6.
'''


class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = [0 for _ in nums]
        ans[0] = nums[0]
        for i in range(1, len(nums)):
            if ans[i - 1] > 0:
                ans[i] = ans[i - 1] + nums[i]
            else:
                ans[i] = nums[i]
        return max(ans)


if __name__ == '__main__':
    s = Solution()
    print(s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
